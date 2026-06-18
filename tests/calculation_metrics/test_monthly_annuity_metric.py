from calculation_metrics.monthly_annuity_metric import MonthlyAnnuityMetric

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