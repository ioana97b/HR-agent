"""Unit tests for get_workforce_analytics tool."""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from tools.hr_tools import _get_workforce_analytics


def test_company_wide_analytics_returns_metrics():
    result = json.loads(_get_workforce_analytics())
    assert "total_headcount" in result
    assert result["total_headcount"] > 0
    assert "average_tenure_years" in result
    assert "average_performance_rating" in result
    assert "average_engagement_score" in result
    assert "headcount_by_department" in result


def test_department_filter_works():
    result = json.loads(_get_workforce_analytics("Engineering"))
    assert "total_headcount" in result
    assert result["total_headcount"] > 0
    # All employees in filtered result should be from Engineering
    assert "Engineering" in result["headcount_by_department"]


def test_invalid_department_returns_error():
    result = json.loads(_get_workforce_analytics("NonExistentDept"))
    assert "error" in result


def test_metrics_are_valid_ranges():
    result = json.loads(_get_workforce_analytics())
    assert 1.0 <= result["average_performance_rating"] <= 5.0
    assert 1.0 <= result["average_engagement_score"] <= 10.0
    assert result["average_tenure_years"] >= 0
