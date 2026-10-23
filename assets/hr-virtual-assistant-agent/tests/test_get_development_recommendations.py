"""Unit tests for get_development_recommendations tool."""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from tools.hr_tools import _get_development_recommendations


def test_valid_employee_returns_recommendations():
    result = json.loads(_get_development_recommendations("E002"))
    assert "recommendations" in result
    assert len(result["recommendations"]) >= 1


def test_recommendations_have_required_fields():
    result = json.loads(_get_development_recommendations("E001"))
    for rec in result["recommendations"]:
        assert "type" in rec
        assert "action" in rec
        assert "priority" in rec
        assert rec["priority"] in ["High", "Medium", "Low"]


def test_low_performer_gets_performance_improvement():
    # E002 has performance_rating=2
    result = json.loads(_get_development_recommendations("E002"))
    types = [r["type"] for r in result["recommendations"]]
    assert "Performance Improvement" in types


def test_high_performer_with_stagnation_gets_promotion_guidance():
    # E001 has performance_rating=4, last_promotion_years_ago=1.5
    result = json.loads(_get_development_recommendations("E001"))
    types = [r["type"] for r in result["recommendations"]]
    assert any(t in ["Promotion Readiness", "Technical Certification", "Cross-Functional Exposure"] for t in types)


def test_invalid_employee_returns_error():
    result = json.loads(_get_development_recommendations("INVALID"))
    assert "error" in result


def test_max_5_recommendations_returned():
    result = json.loads(_get_development_recommendations("E002"))
    assert len(result["recommendations"]) <= 5
