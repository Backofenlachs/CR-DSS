import pytest

from calculation_metrics.total_dti_metric import TotalDtiMetric


def test_total_dti_output_keys():
    metric = TotalDtiMetric()

    assert metric.OUTPUT_KEYS == ["total_dti"]


def test_total_dti_required_inputs():
    metric = TotalDtiMetric()

    assert metric.REQUIRED_INPUTS == [
        "monthly_net_income",
        "existing_monthly_debt_payments"
    ]


def test_total_dti_required_metrics():
    metric = TotalDtiMetric()

    assert metric.REQUIRED_METRICS == [
        "monthly_annuity"
    ]


def test_total_dti_calculation():
    metric = TotalDtiMetric()

    data = {
        "monthly_net_income": 4000,
        "existing_monthly_debt_payments": 500,
        "monthly_annuity": 700
    }

    result = metric.calculate(data)

    assert result["total_dti"] == pytest.approx(0.3)