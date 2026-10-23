"""Unit tests for get_employee_info tool."""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from tools.hr_tools import _get_employee_info


def test_valid_employee_returns_profile():
    result = json.loads(_get_employee_info("E001"))
    assert result["employee_id"] == "E001"
    assert result["name"] == "Alice Chen"
    assert result["department"] == "Engineering"
    assert "performance_rating" in result
    assert "engagement_score" in result
    assert "skills" in result


def test_case_insensitive_employee_id():
    result = json.loads(_get_employee_info("e001"))
    assert result["employee_id"] == "E001"


def test_invalid_employee_returns_error():
    result = json.loads(_get_employee_info("INVALID"))
    assert "error" in result
    assert "INVALID" in result["error"]


def test_manager_employee_returns_profile():
    result = json.loads(_get_employee_info("M001"))
    assert result["employee_id"] == "M001"
    assert result["role"] == "VP Engineering"
