"""Unit tests for answer_hr_policy_question tool."""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from tools.hr_tools import _answer_hr_policy_question


def test_leave_policy_question():
    result = json.loads(_answer_hr_policy_question("How many vacation days do I get?"))
    assert "answer" in result
    assert len(result["answer"]) > 50
    assert "confidence" in result


def test_benefits_question():
    result = json.loads(_answer_hr_policy_question("What health insurance benefits do we have?"))
    assert "answer" in result
    assert result["answer"] != ""


def test_performance_review_question():
    result = json.loads(_answer_hr_policy_question("When is the performance review cycle?"))
    assert "answer" in result
    assert len(result["answer"]) > 50


def test_remote_work_question():
    result = json.loads(_answer_hr_policy_question("What is the remote work policy?"))
    assert "answer" in result
    assert len(result["answer"]) > 50


def test_promotion_question():
    result = json.loads(_answer_hr_policy_question("How do I get promoted?"))
    assert "answer" in result
    assert len(result["answer"]) > 50


def test_unknown_question_returns_fallback():
    result = json.loads(_answer_hr_policy_question("What is the meaning of life?"))
    assert "answer" in result
    # Should return a helpful fallback
    assert len(result["answer"]) > 10


def test_compensation_question():
    result = json.loads(_answer_hr_policy_question("How is the salary band structured?"))
    assert "answer" in result
    assert len(result["answer"]) > 50
