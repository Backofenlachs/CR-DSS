#test_score_result.py

import pytest
from domain.score_result import ScoreResult


def test_score_result_creation():
    breakdown = {
       "income_score": 30,
        "dti_score": 25,
        "employment_score": 20
    }
    
    result = ScoreResult(
        total_score=75,
        risk_category="LOW",
        breakdown=breakdown
    )
    assert result.total_score == 75
    assert result.risk_category == "Low"
    assert result.breakdown == breakdown