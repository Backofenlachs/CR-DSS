import pytest

from calculation_metrics.total_dti_metric import TotalDtiMetric


def valid_data(**overrides):
    data = {
        "monthly_net_income": 4000,
        "existing_monthly_debt_payments": 500,
        "monthly_annuity": 700
    }

    data.update(overrides)
    return data


def test_output_keys():
    metric = TotalDtiMetric()

    assert metric.OUTPUT_KEYS == ["total_dti"]


def test_required_inputs():
    metric = TotalDtiMetric()

    assert metric.REQUIRED_INPUTS == [
        "monthly_net_income",
        "existing_monthly_debt_payments"
    ]


def test_required_metrics():
    metric = TotalDtiMetric()

    assert metric.REQUIRED_METRICS == [
        "monthly_annuity"
    ]


def test_calculation():
    metric = TotalDtiMetric()

    result = metric.calculate(valid_data())

    assert result["total_dti"] == pytest.approx(0.3)


def test_calculation_with_zero_existing_debt_payments():
    metric = TotalDtiMetric()

    result = metric.calculate(valid_data(
        existing_monthly_debt_payments=0,
        monthly_annuity=800,
        monthly_net_income=4000
    ))

    assert result["total_dti"] == pytest.approx(0.2)


def test_calculation_with_zero_monthly_annuity():
    metric = TotalDtiMetric()

    result = metric.calculate(valid_data(
        existing_monthly_debt_payments=500,
        monthly_annuity=0,
        monthly_net_income=4000
    ))

    assert result["total_dti"] == pytest.approx(0.125)


def test_calculation_with_total_dti_greater_than_one():
    metric = TotalDtiMetric()

    result = metric.calculate(valid_data(
        monthly_net_income=2000,
        existing_monthly_debt_payments=1500,
        monthly_annuity=800
    ))

    assert result["total_dti"] == pytest.approx(1.15)


def test_calculation_with_zero_income():
    metric = TotalDtiMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(monthly_net_income=0))


def test_calculation_with_negative_income():
    metric = TotalDtiMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(monthly_net_income=-4000))


def test_calculation_with_negative_debt_payments():
    metric = TotalDtiMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(existing_monthly_debt_payments=-500))


def test_calculation_with_negative_annuity():
    metric = TotalDtiMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(monthly_annuity=-700))


@pytest.mark.parametrize("missing_key", [
    "monthly_net_income",
    "existing_monthly_debt_payments",
    "monthly_annuity"
])
def test_missing_required_data(missing_key):
    metric = TotalDtiMetric()

    data = valid_data()
    data.pop(missing_key)

    with pytest.raises(Exception):
        metric.calculate(data)