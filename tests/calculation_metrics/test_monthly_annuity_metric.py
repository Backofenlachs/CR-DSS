import pytest

from calculation_metrics.monthly_annuity_metric import MonthlyAnnuityMetric


MIN_LOAN_AMOUNT = 500
MAX_LOAN_AMOUNT = 100000
MIN_LOAN_TERM_MONTHS = 1
MAX_LOAN_TERM_MONTHS = 120


def valid_data(**overrides):
    data = {
        "loan_amount": 10000,
        "annual_interest_rate": 0.05,
        "loan_term_months": 12
    }

    data.update(overrides)
    return data


################# contract tests #################

def test_output_keys():
    assert MonthlyAnnuityMetric.OUTPUT_KEYS == [
        "monthly_annuity",
        "total_repayment",
        "total_interest"
    ]


def test_required_inputs():
    assert MonthlyAnnuityMetric.REQUIRED_INPUTS == [
        "loan_amount",
        "annual_interest_rate",
        "loan_term_months"
    ]


def test_required_metrics():
    assert MonthlyAnnuityMetric.REQUIRED_METRICS == []


def test_calculate_returns_all_output_keys():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate(valid_data())

    assert set(result.keys()) == set(MonthlyAnnuityMetric.OUTPUT_KEYS)


################# calculation tests #################

def test_calculation_with_normal_interest():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate(valid_data(
        loan_amount=10000,
        annual_interest_rate=0.05,
        loan_term_months=12
    ))

    assert result["monthly_annuity"] == pytest.approx(856.07, abs=0.01)
    assert result["total_repayment"] == pytest.approx(10272.90, abs=0.01)
    assert result["total_interest"] == pytest.approx(272.90, abs=0.01)


def test_calculation_with_zero_interest():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate(valid_data(
        loan_amount=10000,
        annual_interest_rate=0.0,
        loan_term_months=12
    ))

    assert result["monthly_annuity"] == pytest.approx(833.3333, abs=0.01)
    assert result["total_repayment"] == pytest.approx(10000.0, abs=0.01)
    assert result["total_interest"] == pytest.approx(0.0, abs=0.01)


def test_calculation_with_near_zero_interest():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate(valid_data(
        loan_amount=10000,
        annual_interest_rate=0.000001,
        loan_term_months=12
    ))

    assert result["monthly_annuity"] > 10000 / 12
    assert result["total_repayment"] > 10000
    assert result["total_interest"] > 0


def test_total_repayment_matches_monthly_annuity_times_term():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate(valid_data(
        loan_amount=10000,
        annual_interest_rate=0.05,
        loan_term_months=12
    ))

    assert result["total_repayment"] == pytest.approx(
        result["monthly_annuity"] * 12
    )


def test_total_interest_matches_total_repayment_minus_loan_amount():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate(valid_data(
        loan_amount=10000,
        annual_interest_rate=0.05,
        loan_term_months=12
    ))

    assert result["total_interest"] == pytest.approx(
        result["total_repayment"] - 10000
    )


################# validation tests #################

@pytest.mark.parametrize("missing_key", [
    "loan_amount",
    "annual_interest_rate",
    "loan_term_months"
])
def test_missing_required_input(missing_key):
    metric = MonthlyAnnuityMetric()

    data = valid_data()
    data.pop(missing_key)

    with pytest.raises(ValueError, match="Missing required data"):
        metric.calculate(data)


@pytest.mark.parametrize("invalid_loan_amount", [
    -1000,
    0,
    MIN_LOAN_AMOUNT - 0.01,
    MAX_LOAN_AMOUNT + 0.01
])
def test_invalid_loan_amount(invalid_loan_amount):
    metric = MonthlyAnnuityMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(
            loan_amount=invalid_loan_amount
        ))


@pytest.mark.parametrize("invalid_interest_rate", [
    -0.01,
    -1.0
])
def test_invalid_interest_rate(invalid_interest_rate):
    metric = MonthlyAnnuityMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(
            annual_interest_rate=invalid_interest_rate
        ))


@pytest.mark.parametrize("invalid_loan_term", [
    -12,
    0,
    0.5,
    12.5,
    MAX_LOAN_TERM_MONTHS + 1
])
def test_invalid_loan_term(invalid_loan_term):
    metric = MonthlyAnnuityMetric()

    with pytest.raises(ValueError):
        metric.calculate(valid_data(
            loan_term_months=invalid_loan_term
        ))


################# boundary tests #################

def test_minimum_loan_amount_is_allowed():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate(valid_data(
        loan_amount=MIN_LOAN_AMOUNT
    ))

    assert result["monthly_annuity"] > 0
    assert result["total_repayment"] > 0
    assert result["total_interest"] >= 0


def test_maximum_loan_amount_is_allowed():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate(valid_data(
        loan_amount=MAX_LOAN_AMOUNT
    ))

    assert result["monthly_annuity"] > 0
    assert result["total_repayment"] > 0
    assert result["total_interest"] >= 0


def test_zero_interest_rate_is_allowed():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate(valid_data(
        annual_interest_rate=0.0
    ))

    assert result["monthly_annuity"] == pytest.approx(
        valid_data()["loan_amount"] / valid_data()["loan_term_months"]
    )
    assert result["total_interest"] == pytest.approx(0.0)


def test_minimum_term_is_allowed():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate(valid_data(
        loan_amount=10000,
        annual_interest_rate=0.0,
        loan_term_months=MIN_LOAN_TERM_MONTHS
    ))

    assert result["monthly_annuity"] == pytest.approx(10000.0)
    assert result["total_repayment"] == pytest.approx(10000.0)
    assert result["total_interest"] == pytest.approx(0.0)


def test_maximum_term_is_allowed():
    metric = MonthlyAnnuityMetric()

    result = metric.calculate(valid_data(
        loan_amount=10000,
        annual_interest_rate=0.05,
        loan_term_months=MAX_LOAN_TERM_MONTHS
    ))

    assert result["monthly_annuity"] > 0
    assert result["total_repayment"] > 10000
    assert result["total_interest"] > 0