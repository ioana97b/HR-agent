"""Unit tests for get_attrition_risk tool."""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from tools.hr_tools import _get_attrition_risk


def test_returns_ranked_list():
    result = json.loads(_get_attrition_risk())
    assert "at_risk_employees" in result
    assert "total_evaluated" in result
    assert len(result["at_risk_employees"]) > 0


def test_results_are_sorted_by_risk_score():
    result = json.loads(_get_attrition_risk())
    scores = [e["risk_score"] for e in result["at_risk_employees"]]
    assert scores == sorted(scores, reverse=True)


def test_top_n_parameter_respected():
    result = json.loads(_get_attrition_risk(top_n=3))
    assert result["showing_top"] <= 3
    assert len(result["at_risk_employees"]) <= 3


def test_department_filter_works():
    result = json.loads(_get_attrition_risk(department="Engineering"))
    assert "at_risk_employees" in result
    for emp in result["at_risk_employees"]:
        assert emp["department"] == "Engineering"


def test_each_result_has_required_fields():
    result = json.loads(_get_attrition_risk(top_n=5))
    for emp in result["at_risk_employees"]:
        assert "employee_id" in emp
        assert "risk_score" in emp
        assert "risk_level" in emp
        assert "contributing_factors" in emp
        assert emp["risk_level"] in ["High", "Medium", "Low"]
        assert 0 <= emp["risk_score"] <= 100


def test_invalid_department_returns_error():
    result = json.loads(_get_attrition_risk(department="NoSuchDept"))
    assert "error" in result
