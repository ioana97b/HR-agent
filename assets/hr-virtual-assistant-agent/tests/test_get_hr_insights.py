"""Unit tests for get_hr_insights tool."""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from tools.hr_tools import _get_hr_insights


def test_company_wide_insights_returns_structured_summary():
    result = json.loads(_get_hr_insights())
    assert "scope" in result
    assert "workforce_summary" in result
    assert "performance_highlights" in result
    assert "attrition_risk_breakdown" in result
    assert "key_insights" in result
    assert "recommendations" in result


def test_department_scoped_insights():
    result = json.loads(_get_hr_insights("Engineering"))
    assert result["scope"] == "Engineering"
    assert result["workforce_summary"]["total_headcount"] > 0


def test_key_insights_is_non_empty_list():
    result = json.loads(_get_hr_insights())
    assert isinstance(result["key_insights"], list)
    assert len(result["key_insights"]) >= 1


def test_attrition_risk_breakdown_has_required_fields():
    result = json.loads(_get_hr_insights())
    breakdown = result["attrition_risk_breakdown"]
    assert "high_risk_count" in breakdown
    assert "high_risk_employees" in breakdown
    assert "medium_risk_count" in breakdown
    assert isinstance(breakdown["high_risk_employees"], list)


def test_invalid_scope_returns_error():
    result = json.loads(_get_hr_insights("NoSuchDept"))
    assert "error" in result
