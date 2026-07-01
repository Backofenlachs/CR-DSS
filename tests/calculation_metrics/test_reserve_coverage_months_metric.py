import pytest

from calculation_metrics.reserve_coverage_months_metric import ReserveCoverageMonthsMetric

def valid_data(**overrides):
    data = {
        "monthly_fixed_costs": 1000,
        "existing_monthly_debt_payments": 300,
        "monthly_annuity": 700,
        "cash_reserve": 6000
    }

    data.update(overrides)
    return data

def test_output_keys():
    metric = ReserveCoverageMonthsMetric()

    assert metric.OUTPUT_KEYS == ["reserve_coverage_months"]


def test_required_inputs():
    metric = ReserveCoverageMonthsMetric()

    assert metric.REQUIRED_INPUTS == [
        "monthly_fixed_costs",
        "existing_monthly_debt_payments",
        "cash_reserve"
    ]

def test_required_metrics():
    metric = ReserveCoverageMonthsMetric()

    assert metric.REQUIRED_METRICS == [
        "monthly_annuity"
    ]


def test_calculation():
    metric = ReserveCoverageMonthsMetric()

    result = metric.calculate(valid_data())

    assert result["reserve_coverage_months"] == pytest.approx(3.0)

############ Edge Cases ############
def test_calculation_with_zero_cash_reserve():
    metric = ReserveCoverageMonthsMetric()

    result = metric.calculate(valid_data(cash_reserve=0))

    assert result["reserve_coverage_months"] == 0


def test_calculation_with_zero_monthly_fixed_costs():
    metric = ReserveCoverageMonthsMetric()

    result = metric.calculate(valid_data(monthly_fixed_costs=0))

    assert result["reserve_coverage_months"] == pytest.approx(6.0)


def test_calculation_with_zero_existing_monthly_debt_payments():
    metric = ReserveCoverageMonthsMetric()

    result = metric.calculate(valid_data(existing_monthly_debt_payments=0))

    assert result["reserve_coverage_months"] == pytest.approx(3.529411765)

def test_calculation_with_zero_monthly_annuity():
    metric = ReserveCoverageMonthsMetric()

    result = metric.calculate(valid_data(monthly_annuity=0))

    assert result["reserve_coverage_months"] == pytest.approx(4.615384615)


############ Invalid Cases ############
def test_calculation_with_zero_total_monthly_obligations():
    metric = ReserveCoverageMonthsMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(
            monthly_fixed_costs=0,
            existing_monthly_debt_payments=0,
            monthly_annuity=0
        ))

def test_calculation_with_negative_cash_reserve():
    metric = ReserveCoverageMonthsMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(cash_reserve=-1000))

def test_calculation_with_negative_monthly_fixed_costs():
    metric = ReserveCoverageMonthsMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(monthly_fixed_costs=-1000))

def test_calculation_with_existing_monthly_debt_payments():
    metric = ReserveCoverageMonthsMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(existing_monthly_debt_payments=-1000))

def test_calculation_with_negative_monthly_annuity():
    metric = ReserveCoverageMonthsMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(monthly_annuity=-1000))


@pytest.mark.parametrize("missing_key", [
    "monthly_fixed_costs",
    "existing_monthly_debt_payments",
    "monthly_annuity",
    "cash_reserve"
])
def test_missing_required_data(missing_key):
    metric = ReserveCoverageMonthsMetric()

    data = valid_data()
    data.pop(missing_key)

    with pytest.raises(Exception):
        metric.calculate(data)