"""HR Virtual Assistant tools using simulated HCM data.

All tools are read-only and use in-memory simulated data.
No external API calls are made.
"""

import json
import logging
from typing import Optional

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

import hcm_data

logger = logging.getLogger(__name__)


# ── Input schemas ──────────────────────────────────────────────────────────────

class GetEmployeeInfoInput(BaseModel):
    employee_id: str = Field(description="The unique employee ID (e.g. 'E001')")


class GetWorkforceAnalyticsInput(BaseModel):
    department: Optional[str] = Field(
        default=None,
        description="Optional department name to filter analytics (e.g. 'Engineering', 'Sales'). Leave empty for company-wide metrics."
    )


class GetAttritionRiskInput(BaseModel):
    department: Optional[str] = Field(
        default=None,
        description="Optional department name to filter results (e.g. 'Engineering'). Leave empty for all departments."
    )
    top_n: int = Field(
        default=10,
        description="Number of top at-risk employees to return (max 50).",
        ge=1,
        le=50,
    )


class GetDevelopmentRecommendationsInput(BaseModel):
    employee_id: str = Field(description="The unique employee ID to generate recommendations for (e.g. 'E002')")


class GetHrInsightsInput(BaseModel):
    scope: Optional[str] = Field(
        default="all",
        description="Scope of insights: 'all' for company-wide, or a specific department name (e.g. 'Engineering')."
    )


class AnswerHrPolicyQuestionInput(BaseModel):
    question: str = Field(description="The HR policy question to answer (e.g. 'How many vacation days do I get?')")


# ── Tool implementations ───────────────────────────────────────────────────────

def _get_employee_info(employee_id: str) -> str:
    """Retrieve an employee's profile from simulated HCM data."""
    logger.info("[M1.achieved]: HR Q&A tool invoked - retrieving employee info for %s", employee_id)
    employee = hcm_data.get_employee_by_id(employee_id)
    if not employee:
        logger.warning("[M1.missed]: Employee info retrieval failed - employee %s not found", employee_id)
        return json.dumps({"error": f"Employee with ID '{employee_id}' not found. Please check the ID and try again."})
    return json.dumps(employee, indent=2)


def _get_workforce_analytics(department: Optional[str] = None) -> str:
    """Return workforce analytics metrics for the specified department or company-wide."""
    logger.info("[M2.achieved]: Workforce analytics tool invoked - department=%s", department or "all")
    summary = hcm_data.get_workforce_summary(department)
    if "error" in summary:
        logger.warning("[M2.missed]: Workforce analytics tool failed - %s", summary["error"])
    return json.dumps(summary, indent=2)


def _get_attrition_risk(department: Optional[str] = None, top_n: int = 10) -> str:
    """Return ranked list of employees at attrition risk with scores and contributing factors."""
    employees = hcm_data.get_department_employees(department) if department else hcm_data.get_all_employees()
    if not employees:
        logger.warning("[M3.missed]: Attrition risk tool - no employees found for department '%s'", department)
        return json.dumps({"error": f"No employees found for department '{department}'"})

    risk_results = []
    for emp in employees:
        risk = hcm_data.compute_attrition_risk(emp["employee_id"])
        if "error" not in risk:
            risk_results.append(risk)

    risk_results.sort(key=lambda x: x["risk_score"], reverse=True)
    top_n = min(top_n, 50)
    result = risk_results[:top_n]

    logger.info("[M3.achieved]: Attrition risk scoring tool returned %d results", len(result))
    return json.dumps({
        "total_evaluated": len(risk_results),
        "showing_top": len(result),
        "at_risk_employees": result,
    }, indent=2)


def _get_development_recommendations(employee_id: str) -> str:
    """Generate personalised development recommendations for an employee."""
    plan = hcm_data.get_development_plan(employee_id)
    if "error" in plan:
        logger.warning("[M4.missed]: Development recommendation tool failed - %s", plan["error"])
        return json.dumps(plan)
    logger.info("[M4.achieved]: Development recommendation tool returned %d recommendations for %s", len(plan.get("recommendations", [])), employee_id)
    return json.dumps(plan, indent=2)


def _get_hr_insights(scope: Optional[str] = "all") -> str:
    """Generate a structured HR health insight narrative."""
    dept = None if scope == "all" else scope
    summary = hcm_data.get_workforce_summary(dept)

    if "error" in summary:
        logger.warning("[M5.missed]: HR insight reporting tool failed - %s", summary["error"])
        return json.dumps(summary)

    # Compute attrition risk breakdown
    employees = hcm_data.get_department_employees(dept) if dept else hcm_data.get_all_employees()
    high_risk = [e for e in employees if hcm_data.compute_attrition_risk(e["employee_id"]).get("risk_level") == "High"]
    medium_risk = [e for e in employees if hcm_data.compute_attrition_risk(e["employee_id"]).get("risk_level") == "Medium"]
    low_performers = [e for e in employees if e["performance_rating"] <= 2]
    top_performers = [e for e in employees if e["performance_rating"] == 5]

    insight = {
        "scope": scope or "all",
        "workforce_summary": summary,
        "performance_highlights": {
            "top_performers_count": len(top_performers),
            "top_performer_names": [e["name"] for e in top_performers],
            "low_performers_count": len(low_performers),
            "low_performer_names": [e["name"] for e in low_performers],
        },
        "attrition_risk_breakdown": {
            "high_risk_count": len(high_risk),
            "high_risk_employees": [{"id": e["employee_id"], "name": e["name"], "department": e["department"]} for e in high_risk],
            "medium_risk_count": len(medium_risk),
        },
        "key_insights": [],
        "recommendations": [],
    }

    # Generate narrative insights
    if len(high_risk) > 0:
        insight["key_insights"].append(f"{len(high_risk)} employee(s) are at high attrition risk and need immediate attention.")
    if summary["average_engagement_score"] < 6:
        insight["key_insights"].append(f"Average engagement score is {summary['average_engagement_score']}/10 — below the healthy threshold of 7.")
    if summary["average_performance_rating"] < 3.5:
        insight["key_insights"].append(f"Average performance rating is {summary['average_performance_rating']}/5 — improvement actions are recommended.")
    if not insight["key_insights"]:
        insight["key_insights"].append("Workforce health looks broadly positive — continue monitoring engagement and performance trends.")

    if len(high_risk) > 0:
        insight["recommendations"].append("Schedule 1-on-1 retention conversations with high-risk employees this month.")
    if summary["average_engagement_score"] < 6:
        insight["recommendations"].append("Run an engagement pulse survey to identify root causes of low engagement scores.")

    logger.info("[M5.achieved]: HR insight reporting tool returned structured summary for scope '%s'", scope)
    return json.dumps(insight, indent=2)


def _answer_hr_policy_question(question: str) -> str:
    """Answer a common HR policy question using the built-in knowledge base."""
    logger.info("[M1.achieved]: HR policy Q&A tool invoked with question: %s", question[:80])
    result = hcm_data.match_policy_question(question)
    if result.get("confidence") == "low":
        logger.warning("[M1.missed]: HR policy Q&A tool - low confidence match for question: %s", question[:80])
    return json.dumps(result)


# ── Tool instances ─────────────────────────────────────────────────────────────

def get_hr_tools() -> list[StructuredTool]:
    """Return all HR virtual assistant tools."""
    return [
        StructuredTool.from_function(
            func=_get_employee_info,
            name="get_employee_info",
            description="Retrieve an employee's profile including role, department, tenure, performance rating, engagement score, and skills. Requires the employee ID.",
            args_schema=GetEmployeeInfoInput,
        ),
        StructuredTool.from_function(
            func=_get_workforce_analytics,
            name="get_workforce_analytics",
            description="Get workforce analytics metrics: headcount, average tenure, average performance rating, average engagement score, attrition risk rate, and headcount by department. Optionally filter by department.",
            args_schema=GetWorkforceAnalyticsInput,
        ),
        StructuredTool.from_function(
            func=_get_attrition_risk,
            name="get_attrition_risk",
            description="Get a ranked list of employees at attrition risk with their risk score (0-100), risk level (High/Medium/Low), and contributing factors. Optionally filter by department and specify how many top results to return.",
            args_schema=GetAttritionRiskInput,
        ),
        StructuredTool.from_function(
            func=_get_development_recommendations,
            name="get_development_recommendations",
            description="Generate personalised development recommendations for a specific employee based on their performance rating, engagement score, skills, and career progression. Requires the employee ID.",
            args_schema=GetDevelopmentRecommendationsInput,
        ),
        StructuredTool.from_function(
            func=_get_hr_insights,
            name="get_hr_insights",
            description="Generate a structured HR health insight report covering workforce summary, performance highlights, attrition risk breakdown, key insights, and actionable recommendations. Scope can be 'all' (company-wide) or a specific department name.",
            args_schema=GetHrInsightsInput,
        ),
        StructuredTool.from_function(
            func=_answer_hr_policy_question,
            name="answer_hr_policy_question",
            description="Answer a common HR policy question (e.g. leave policy, benefits, performance reviews, compensation, onboarding, remote work, promotions). Use this for any HR policy or procedure question from employees.",
            args_schema=AnswerHrPolicyQuestionInput,
        ),
    ]
