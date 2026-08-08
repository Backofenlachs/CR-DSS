import pytest

from calculation_metrics.residual_income_metric import ResidualIncomeAfterLoanMetric

def valid_data(**overrides):
    data = {
        "monthly_net_income": 4000,
        "monthly_fixed_costs": 1000,
        "existing_monthly_debt_payments": 500,
        "monthly_annuity": 800
    }
    data.update(overrides)
    return data

def test_output_keys():
    metric = ResidualIncomeAfterLoanMetric()

    assert metric.OUTPUT_KEYS == ["residual_income_after_loan"]

def test_required_inputs():
    metric = ResidualIncomeAfterLoanMetric()

    assert metric.REQUIRED_INPUTS == [
        "monthly_net_income",
        "monthly_fixed_costs",
        "existing_monthly_debt_payments",
    ]

def test_required_metrics():
    metric = ResidualIncomeAfterLoanMetric()

    assert metric.REQUIRED_METRICS == [
        "monthly_annuity"
    ]

def test_calculation():
    metric = ResidualIncomeAfterLoanMetric()

    result = metric.calculate(valid_data())

############# Edge Cases ############