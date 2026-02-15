#test_score_result.py

import pytest
from domain.score_result import ScoreResult


test_breakdown = {
    "income_score": 30,
    "dti_score": 25,
    "employment_score": 20
}

test_total_score=75,
test_risk_category="LOW",

def test_score_result_creation():
    
    result = ScoreResult(
        total_score=test_total_score,
        risk_category=test_risk_category,
        breakdown=test_breakdown
    )
    assert result.total_score == test_total_score
    assert result.risk_category == test_risk_category
    assert result.breakdown == test_breakdown