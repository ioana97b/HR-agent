"""Simulated HCM (Human Capital Management) data module.

Provides in-memory employee data and policy knowledge base for the HR Virtual Assistant.
All data is simulated and for demonstration purposes only.
"""

from typing import Any

# Simulated employee dataset
_EMPLOYEES = [
    {"employee_id": "E001", "name": "Alice Chen", "department": "Engineering", "role": "Senior Software Engineer", "tenure_years": 3.5, "performance_rating": 4, "engagement_score": 8, "skills": ["Python", "AWS", "Kubernetes"], "manager_id": "M001", "last_promotion_years_ago": 1.5, "salary_band": "L5", "status": "active"},
    {"employee_id": "E002", "name": "Bob Martinez", "department": "Engineering", "role": "Software Engineer", "tenure_years": 5.2, "performance_rating": 2, "engagement_score": 4, "skills": ["Java", "Spring Boot"], "manager_id": "M001", "last_promotion_years_ago": 4.0, "salary_band": "L4", "status": "at-risk"},
    {"employee_id": "E003", "name": "Carol White", "department": "HR", "role": "HR Business Partner", "tenure_years": 2.0, "performance_rating": 5, "engagement_score": 9, "skills": ["Talent Management", "SuccessFactors"], "manager_id": "M002", "last_promotion_years_ago": 0.5, "salary_band": "L4", "status": "active"},
    {"employee_id": "E004", "name": "David Kim", "department": "Sales", "role": "Account Executive", "tenure_years": 1.2, "performance_rating": 3, "engagement_score": 7, "skills": ["CRM", "Negotiation", "SaaS Sales"], "manager_id": "M003", "last_promotion_years_ago": 1.2, "salary_band": "L3", "status": "active"},
    {"employee_id": "E005", "name": "Eva Patel", "department": "Finance", "role": "Financial Analyst", "tenure_years": 4.8, "performance_rating": 2, "engagement_score": 3, "skills": ["Excel", "SAP S/4HANA", "Financial Modeling"], "manager_id": "M004", "last_promotion_years_ago": 4.5, "salary_band": "L4", "status": "at-risk"},
    {"employee_id": "E006", "name": "Frank Brown", "department": "Engineering", "role": "DevOps Engineer", "tenure_years": 2.8, "performance_rating": 4, "engagement_score": 7, "skills": ["CI/CD", "Terraform", "Docker"], "manager_id": "M001", "last_promotion_years_ago": 1.0, "salary_band": "L4", "status": "active"},
    {"employee_id": "E007", "name": "Grace Liu", "department": "Marketing", "role": "Marketing Manager", "tenure_years": 6.1, "performance_rating": 2, "engagement_score": 4, "skills": ["Campaign Management", "Analytics", "SEO"], "manager_id": "M005", "last_promotion_years_ago": 5.0, "salary_band": "L5", "status": "at-risk"},
    {"employee_id": "E008", "name": "Henry Nguyen", "department": "Sales", "role": "Sales Manager", "tenure_years": 3.3, "performance_rating": 5, "engagement_score": 9, "skills": ["Team Leadership", "Pipeline Management", "CRM"], "manager_id": "M003", "last_promotion_years_ago": 0.8, "salary_band": "L6", "status": "active"},
    {"employee_id": "E009", "name": "Iris Johansson", "department": "Engineering", "role": "Principal Engineer", "tenure_years": 7.0, "performance_rating": 5, "engagement_score": 8, "skills": ["Architecture", "Python", "Microservices"], "manager_id": "M001", "last_promotion_years_ago": 2.0, "salary_band": "L7", "status": "active"},
    {"employee_id": "E010", "name": "James O'Brien", "department": "HR", "role": "Recruiter", "tenure_years": 1.5, "performance_rating": 3, "engagement_score": 6, "skills": ["Sourcing", "Interviewing", "ATS"], "manager_id": "M002", "last_promotion_years_ago": 1.5, "salary_band": "L3", "status": "active"},
    {"employee_id": "E011", "name": "Karen Wilson", "department": "Finance", "role": "Senior Accountant", "tenure_years": 8.2, "performance_rating": 3, "engagement_score": 5, "skills": ["GAAP", "SAP FI", "Auditing"], "manager_id": "M004", "last_promotion_years_ago": 6.0, "salary_band": "L5", "status": "at-risk"},
    {"employee_id": "E012", "name": "Liam Davis", "department": "Engineering", "role": "Data Engineer", "tenure_years": 2.1, "performance_rating": 4, "engagement_score": 8, "skills": ["Spark", "Kafka", "Python", "SQL"], "manager_id": "M001", "last_promotion_years_ago": 2.1, "salary_band": "L4", "status": "active"},
    {"employee_id": "E013", "name": "Mia Russo", "department": "Marketing", "role": "Content Strategist", "tenure_years": 3.7, "performance_rating": 4, "engagement_score": 7, "skills": ["Content Writing", "SEO", "Analytics"], "manager_id": "M005", "last_promotion_years_ago": 1.5, "salary_band": "L4", "status": "active"},
    {"employee_id": "E014", "name": "Noah Thompson", "department": "Sales", "role": "Sales Development Representative", "tenure_years": 0.8, "performance_rating": 3, "engagement_score": 7, "skills": ["Cold Calling", "LinkedIn Sales Navigator"], "manager_id": "M003", "last_promotion_years_ago": 0.8, "salary_band": "L2", "status": "active"},
    {"employee_id": "E015", "name": "Olivia Park", "department": "Engineering", "role": "QA Engineer", "tenure_years": 4.0, "performance_rating": 2, "engagement_score": 4, "skills": ["Selenium", "API Testing", "JIRA"], "manager_id": "M001", "last_promotion_years_ago": 3.5, "salary_band": "L4", "status": "at-risk"},
    {"employee_id": "E016", "name": "Paul Edwards", "department": "Finance", "role": "Controller", "tenure_years": 9.0, "performance_rating": 4, "engagement_score": 7, "skills": ["IFRS", "SAP CO", "Treasury"], "manager_id": "M004", "last_promotion_years_ago": 2.5, "salary_band": "L7", "status": "active"},
    {"employee_id": "E017", "name": "Quinn Foster", "department": "HR", "role": "Learning & Development Specialist", "tenure_years": 2.5, "performance_rating": 4, "engagement_score": 8, "skills": ["Instructional Design", "LMS Administration", "SuccessFactors Learning"], "manager_id": "M002", "last_promotion_years_ago": 1.0, "salary_band": "L4", "status": "active"},
    {"employee_id": "E018", "name": "Rachel Gomez", "department": "Marketing", "role": "Digital Marketing Specialist", "tenure_years": 5.5, "performance_rating": 2, "engagement_score": 3, "skills": ["Paid Ads", "Google Analytics", "Email Marketing"], "manager_id": "M005", "last_promotion_years_ago": 5.0, "salary_band": "L4", "status": "at-risk"},
    {"employee_id": "E019", "name": "Samuel Lee", "department": "Engineering", "role": "Machine Learning Engineer", "tenure_years": 1.8, "performance_rating": 5, "engagement_score": 9, "skills": ["PyTorch", "Python", "MLOps"], "manager_id": "M001", "last_promotion_years_ago": 1.8, "salary_band": "L5", "status": "active"},
    {"employee_id": "E020", "name": "Tina Moreau", "department": "Sales", "role": "Senior Account Executive", "tenure_years": 4.5, "performance_rating": 5, "engagement_score": 9, "skills": ["Enterprise Sales", "MEDDIC", "CRM"], "manager_id": "M003", "last_promotion_years_ago": 1.0, "salary_band": "L6", "status": "active"},
    # Managers
    {"employee_id": "M001", "name": "Alex Turner", "department": "Engineering", "role": "VP Engineering", "tenure_years": 5.0, "performance_rating": 5, "engagement_score": 9, "skills": ["Engineering Leadership", "Architecture", "Agile"], "manager_id": "EXEC", "last_promotion_years_ago": 1.0, "salary_band": "L8", "status": "active"},
    {"employee_id": "M002", "name": "Sandra Mills", "department": "HR", "role": "HR Director", "tenure_years": 7.0, "performance_rating": 4, "engagement_score": 8, "skills": ["HR Strategy", "Talent Management", "Compliance"], "manager_id": "EXEC", "last_promotion_years_ago": 3.0, "salary_band": "L8", "status": "active"},
    {"employee_id": "M003", "name": "Tom Richards", "department": "Sales", "role": "VP Sales", "tenure_years": 6.0, "performance_rating": 5, "engagement_score": 8, "skills": ["Sales Strategy", "Revenue Operations", "Team Leadership"], "manager_id": "EXEC", "last_promotion_years_ago": 2.0, "salary_band": "L8", "status": "active"},
    {"employee_id": "M004", "name": "Uma Singh", "department": "Finance", "role": "CFO", "tenure_years": 8.0, "performance_rating": 5, "engagement_score": 8, "skills": ["Financial Strategy", "IFRS", "Investor Relations"], "manager_id": "EXEC", "last_promotion_years_ago": 1.5, "salary_band": "L9", "status": "active"},
    {"employee_id": "M005", "name": "Victor Dubois", "department": "Marketing", "role": "CMO", "tenure_years": 4.5, "performance_rating": 4, "engagement_score": 7, "skills": ["Brand Strategy", "Demand Generation", "Product Marketing"], "manager_id": "EXEC", "last_promotion_years_ago": 2.0, "salary_band": "L9", "status": "active"},
]

# HR policy knowledge base
_HR_POLICIES = {
    "leave": {
        "keywords": ["leave", "vacation", "holiday", "pto", "time off", "annual leave", "sick leave", "parental leave", "maternity", "paternity"],
        "answer": (
            "**Leave Policy Summary:**\n"
            "- **Annual Leave**: 25 days per year (pro-rated for part-time). Carry over up to 5 days to the next year.\n"
            "- **Sick Leave**: 10 days per year, no carry-over. Medical certificate required after 3 consecutive days.\n"
            "- **Parental Leave**: 16 weeks fully paid for primary caregiver; 4 weeks for secondary caregiver.\n"
            "- **Public Holidays**: 11 paid public holidays per year.\n"
            "- **Leave Requests**: Submit via the HR portal at least 2 weeks in advance for planned leave.\n"
            "- **Emergency Leave**: Up to 3 days per year for personal emergencies, with manager approval."
        )
    },
    "benefits": {
        "keywords": ["benefits", "health insurance", "dental", "vision", "retirement", "pension", "401k", "gym", "wellness"],
        "answer": (
            "**Benefits Package Summary:**\n"
            "- **Health Insurance**: Comprehensive medical, dental, and vision coverage for employees and dependents.\n"
            "- **Retirement**: Company matches 4% of salary into the company pension plan.\n"
            "- **Wellness**: Monthly wellness allowance of $100 for gym, fitness, or mental health services.\n"
            "- **Learning & Development**: Annual L&D budget of $2,000 per employee for courses, certifications, and conferences.\n"
            "- **Employee Assistance Program (EAP)**: Free confidential counseling and support services.\n"
            "- **Life Insurance**: 2x annual salary, paid by the company."
        )
    },
    "performance_review": {
        "keywords": ["performance review", "review cycle", "evaluation", "appraisal", "feedback", "rating", "assessment"],
        "answer": (
            "**Performance Review Cycle:**\n"
            "- **Cadence**: Annual performance reviews in December, with mid-year check-ins in June.\n"
            "- **Process**: Employees complete a self-assessment → Manager completes evaluation → Calibration session → Final rating shared.\n"
            "- **Ratings**: 1 (Needs Improvement) to 5 (Exceptional). Ratings of 3+ are considered 'meeting expectations'.\n"
            "- **Outcome**: Performance ratings influence bonus payouts and eligibility for promotion.\n"
            "- **Continuous Feedback**: Managers and peers can provide continuous feedback year-round via the HR portal."
        )
    },
    "compensation": {
        "keywords": ["salary", "compensation", "pay", "bonus", "raise", "increment", "salary band", "pay grade"],
        "answer": (
            "**Compensation Policy:**\n"
            "- **Salary Bands**: Roles are mapped to salary bands L1–L10. Bands are reviewed annually against market benchmarks.\n"
            "- **Annual Increases**: Merit increases are awarded during the annual review cycle based on performance rating and position within band.\n"
            "- **Bonus**: Target annual bonus ranges from 5% (L1-L3) to 20% (L7+) of base salary, based on company and individual performance.\n"
            "- **Equity**: Senior roles (L6+) may receive equity grants reviewed every 2 years.\n"
            "- **Pay Transparency**: Employees can view their salary band range in the HR portal."
        )
    },
    "onboarding": {
        "keywords": ["onboarding", "new hire", "first day", "orientation", "joining", "start date"],
        "answer": (
            "**Onboarding Process:**\n"
            "- **Pre-boarding**: IT equipment and system access are set up 3 days before start date. Welcome email sent with day-1 instructions.\n"
            "- **Week 1**: Company orientation, HR admin (ID, payroll, benefits enrollment), and team introductions.\n"
            "- **30-Day Plan**: Role-specific onboarding plan with key stakeholder meetings and training.\n"
            "- **90-Day Check-in**: Formal check-in with manager and HR to review progress and address any concerns.\n"
            "- **Buddy Programme**: Every new hire is assigned an onboarding buddy from their team."
        )
    },
    "remote_work": {
        "keywords": ["remote", "work from home", "wfh", "hybrid", "flexible working", "office attendance"],
        "answer": (
            "**Remote & Hybrid Work Policy:**\n"
            "- **Hybrid Model**: Employees are expected to be in the office at least 3 days per week.\n"
            "- **Remote Days**: Up to 2 days per week of remote work are permitted with manager agreement.\n"
            "- **Fully Remote**: Fully remote arrangements require VP-level approval and are reviewed annually.\n"
            "- **International Remote**: Working from another country for more than 30 days requires HR and Legal approval.\n"
            "- **Equipment**: Home office equipment allowance of $500 for fully remote employees."
        )
    },
    "promotion": {
        "keywords": ["promotion", "career progression", "advancement", "level up", "grow", "career path"],
        "answer": (
            "**Promotion & Career Progression:**\n"
            "- **Eligibility**: Typically requires 1+ year in current role with performance rating of 4 or 5.\n"
            "- **Process**: Manager nominates employee → HR calibration → Business case approved by VP → Offer letter issued.\n"
            "- **Timeline**: Promotions are typically processed twice per year: July and January.\n"
            "- **Career Ladders**: Each department has a published career ladder. Employees can view their progression path in the HR portal.\n"
            "- **Internal Mobility**: Employees are encouraged to apply for internal roles after 12 months in their current position."
        )
    },
}


def get_all_employees() -> list[dict[str, Any]]:
    """Return all employees."""
    return list(_EMPLOYEES)


def get_employee_by_id(employee_id: str) -> dict[str, Any] | None:
    """Return a single employee by ID."""
    for emp in _EMPLOYEES:
        if emp["employee_id"].upper() == employee_id.upper():
            return emp
    return None


def get_department_employees(department: str) -> list[dict[str, Any]]:
    """Return employees in a given department (case-insensitive match)."""
    return [e for e in _EMPLOYEES if e["department"].lower() == department.lower()]


def get_workforce_summary(department: str | None = None) -> dict[str, Any]:
    """Return workforce summary metrics, optionally filtered by department."""
    employees = get_department_employees(department) if department else list(_EMPLOYEES)
    if not employees:
        return {"error": f"No employees found for department '{department}'"}

    total = len(employees)
    at_risk_count = sum(1 for e in employees if e["status"] == "at-risk")
    avg_tenure = round(sum(e["tenure_years"] for e in employees) / total, 1)
    avg_performance = round(sum(e["performance_rating"] for e in employees) / total, 2)
    avg_engagement = round(sum(e["engagement_score"] for e in employees) / total, 2)

    departments = {}
    for e in employees:
        dept = e["department"]
        departments[dept] = departments.get(dept, 0) + 1

    return {
        "total_headcount": total,
        "at_risk_count": at_risk_count,
        "attrition_risk_rate": f"{round(at_risk_count / total * 100, 1)}%",
        "average_tenure_years": avg_tenure,
        "average_performance_rating": avg_performance,
        "average_engagement_score": avg_engagement,
        "headcount_by_department": departments,
    }


def compute_attrition_risk(employee_id: str) -> dict[str, Any]:
    """Compute attrition risk score and contributing factors for an employee."""
    emp = get_employee_by_id(employee_id)
    if not emp:
        return {"error": f"Employee '{employee_id}' not found"}

    score = 0
    factors = []

    # Low performance is a key predictor
    if emp["performance_rating"] <= 2:
        score += 35
        factors.append(f"Low performance rating ({emp['performance_rating']}/5)")
    elif emp["performance_rating"] == 3:
        score += 10
        factors.append("Average performance — at risk if unaddressed")

    # Low engagement
    if emp["engagement_score"] <= 4:
        score += 30
        factors.append(f"Low engagement score ({emp['engagement_score']}/10)")
    elif emp["engagement_score"] <= 6:
        score += 10
        factors.append(f"Moderate engagement ({emp['engagement_score']}/10)")

    # Long time since last promotion relative to tenure
    if emp["last_promotion_years_ago"] > 3 and emp["tenure_years"] > 3:
        score += 25
        factors.append(f"No promotion in {emp['last_promotion_years_ago']} years (tenure: {emp['tenure_years']} years)")

    # Stagnation at same salary band for long time
    if emp["tenure_years"] > 4 and emp["last_promotion_years_ago"] > 3:
        score += 10
        factors.append("Career stagnation risk — long tenure without advancement")

    # Normalize score to 0–100
    score = min(score, 100)

    if score >= 60:
        risk_level = "High"
    elif score >= 30:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "employee_id": emp["employee_id"],
        "name": emp["name"],
        "department": emp["department"],
        "role": emp["role"],
        "risk_score": score,
        "risk_level": risk_level,
        "contributing_factors": factors if factors else ["No significant risk factors identified"],
    }


def get_development_plan(employee_id: str) -> dict[str, Any]:
    """Generate development recommendations for an employee."""
    emp = get_employee_by_id(employee_id)
    if not emp:
        return {"error": f"Employee '{employee_id}' not found"}

    recommendations = []

    # Based on performance
    if emp["performance_rating"] <= 2:
        recommendations.append({
            "type": "Performance Improvement",
            "action": "Enroll in structured performance coaching program with monthly check-ins.",
            "priority": "High",
        })
    elif emp["performance_rating"] == 3:
        recommendations.append({
            "type": "Skill Enhancement",
            "action": f"Identify one key skill gap in your current role and complete a targeted online course within 90 days.",
            "priority": "Medium",
        })

    # Based on role-specific skills
    role = emp["role"].lower()
    if "engineer" in role or "developer" in role:
        missing_cloud = not any(s in ["AWS", "GCP", "Azure", "Kubernetes"] for s in emp["skills"])
        if missing_cloud:
            recommendations.append({
                "type": "Technical Certification",
                "action": "Pursue AWS or Azure cloud certification to strengthen cloud architecture skills.",
                "priority": "Medium",
            })
        if "Python" not in emp["skills"] and "Java" not in emp["skills"]:
            recommendations.append({
                "type": "Language Proficiency",
                "action": "Complete an advanced Python or Java course to diversify technical toolkit.",
                "priority": "Medium",
            })
    elif "manager" in role or "director" in role or "vp" in role or "lead" in role:
        recommendations.append({
            "type": "Leadership Development",
            "action": "Complete the internal 'Effective Manager' programme, focusing on feedback and coaching techniques.",
            "priority": "Medium",
        })
    elif "sales" in role:
        recommendations.append({
            "type": "Sales Methodology",
            "action": "Complete MEDDIC or SPIN Selling certification to improve deal qualification and close rates.",
            "priority": "Medium",
        })
    elif "analyst" in role or "finance" in role or "account" in role:
        recommendations.append({
            "type": "Financial Acumen",
            "action": "Pursue SAP S/4HANA Finance or IFRS certification to deepen technical financial expertise.",
            "priority": "Medium",
        })

    # Career advancement
    if emp["last_promotion_years_ago"] >= 1.5 and emp["performance_rating"] >= 4:
        recommendations.append({
            "type": "Promotion Readiness",
            "action": f"Based on your tenure and performance, discuss a promotion roadmap with your manager. Document key achievements from the last 12 months.",
            "priority": "High",
        })

    # Engagement
    if emp["engagement_score"] <= 5:
        recommendations.append({
            "type": "Engagement & Wellbeing",
            "action": "Schedule a career conversation with your HR Business Partner to align personal goals with team opportunities. Explore internal mobility options.",
            "priority": "High",
        })

    # Cross-functional exposure
    if emp["tenure_years"] >= 2 and len(recommendations) < 5:
        recommendations.append({
            "type": "Cross-Functional Exposure",
            "action": "Volunteer for a cross-departmental project or internal task force to broaden business knowledge and expand your network.",
            "priority": "Low",
        })

    return {
        "employee_id": emp["employee_id"],
        "name": emp["name"],
        "role": emp["role"],
        "department": emp["department"],
        "performance_rating": emp["performance_rating"],
        "engagement_score": emp["engagement_score"],
        "recommendations": recommendations[:5],  # Cap at 5
    }


def match_policy_question(question: str) -> dict[str, Any]:
    """Match a question to the best policy answer using keyword matching."""
    question_lower = question.lower()
    best_match = None
    best_score = 0

    for _topic, policy in _HR_POLICIES.items():
        score = sum(1 for kw in policy["keywords"] if kw in question_lower)
        if score > best_score:
            best_score = score
            best_match = policy

    if best_match and best_score > 0:
        return {"answer": best_match["answer"], "confidence": "high" if best_score >= 2 else "medium"}

    # Default fallback
    available = ", ".join(k.replace("_", " ") for k in _HR_POLICIES)
    return {
        "answer": (
            f"I could not find a specific policy match for your question. "
            f"I have information on the following HR topics: {available}. "
            f"Please rephrase your question or contact HR directly at hr@company.com."
        ),
        "confidence": "low",
    }
