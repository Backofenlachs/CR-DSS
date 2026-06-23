import pytest
from calculation_metrics.monthly_annuity_metric import MonthlyAnnuityMetric

# contract tests
def test_output_keys():
    assert MonthlyAnnuityMetric.OUTPUT_KEYS == [
        "monthly_annuity",
        "total_repayment",
        "total_interest"
    ]

def test_calculate_returns_all_output_keys():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate({
        "loan_amount": 10000,
        "annual_interest_rate": 0.05,
        "loan_term_months": 12
    })

    assert set(result.keys()) == set(MonthlyAnnuityMetric.OUTPUT_KEYS)


################# calculation tests #################
def test_calculation_with_normal_interest():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate({
        "loan_amount": 10000,
        "annual_interest_rate": 0.05,
        "loan_term_months": 12
    })

    assert result["monthly_annuity"] == pytest.approx(856.07, abs=0.01)
    assert result["total_repayment"] == pytest.approx(10272.90, abs=0.01)
    assert result["total_interest"] == pytest.approx(272.90, abs=0.01)


import pytest

def test_calculation_with_zero_interest():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate({
        "loan_amount": 10000,
        "annual_interest_rate": 0.0,
        "loan_term_months": 12
    })

    assert result["monthly_annuity"] == pytest.approx(833.3333, abs=0.01)
    assert result["total_repayment"] == pytest.approx(10000.0, abs=0.01)
    assert result["total_interest"] == pytest.approx(0.0, abs=0.01)


def test_calculation_with_near_zero_interest():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate({
        "loan_amount": 10000,
        "annual_interest_rate": 0.000001,
        "loan_term_months": 12
    })

    assert result["monthly_annuity"] > 833.33
    assert result["total_interest"] > 0


################# validation tests #################

def test_missing_input():
    metric = MonthlyAnnuityMetric()

    with pytest.raises(ValueError, match="Missing required data"):
        metric.calculate({
            "annual_interest_rate": 0.05,
            "loan_term_months": 12
        })

def test_invalid_loan_amount():
    pass

def test_invalid_interest_rate():
    pass

def test_invalid_loan_term():
    pass

################# boundary tests #################
def test_minimum_loan_amount_is_allowed():
    pass

def test_maximum_loan_amount_is_allowed():
    pass

def test_minimum_term_is_allowed():
    pass

def test_maximum_term_is_allowed():
    pass