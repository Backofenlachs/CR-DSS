from calculation_metrics.calculation_metric import CalculationMetric

class ReserveCoverageMonthsMetric(CalculationMetric):

    OUTPUT_KEYS = [
        "reserve_coverage_months"
    ]

    REQUIRED_INPUTS = [
        "monthly_fixed_costs",
        "existing_monthly_debt_payments",
        "cash_reserve"
    ]

    REQUIRED_METRICS = [
        "monthly_annuity"
    ]

    def calculate(self, data):
        
        total_monthly_obligations = (
            data["monthly_fixed_costs"] +
            data["existing_monthly_debt_payments"] +
            data["monthly_annuity"]
        )

        reserve_coverage_months = data["cash_reserve"] / total_monthly_obligations
        
        return {
            "reserve_coverage_months": reserve_coverage_months
        }
