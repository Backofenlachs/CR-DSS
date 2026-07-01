from calculation_metrics.calculation_metric import CalculationMetric

class ReserveCoverageMonthsMetric(CalculationMetric):
    NAME = "reserve_coverage_months"
    
    REQUIRED_INPUTS = [
        "monthly_fixed_costs",
        "existing_monthly_debt_payments",
        "cash_reserve"
    ]

    REQUIRED_METRICS = [
        "monthly_annuity"
    ]

    OUTPUT_KEYS = [
        "reserve_coverage_months"
    ]


    def _calculate(self, data):
        
        if data["monthly_fixed_costs"] < 0:
            raise ValueError("monthly_fixed_costs must not be negative")
        
        if data["existing_monthly_debt_payments"] < 0:
            raise ValueError("existing_monthly_debt_payments must not be negative")
        
        if data["monthly_annuity"] < 0:
            raise ValueError("monthly_annuity must not be negative")
        
        if data["cash_reserve"] < 0:
            raise ValueError("cash_reserve must not be negative")

        total_monthly_obligations = (
            data["monthly_fixed_costs"] 
            + data["existing_monthly_debt_payments"]
            + data["monthly_annuity"]
        )

        if total_monthly_obligations <= 0:
            raise ValueError("Total monthly obligations must be greater than 0 to calculate reserve coverage months")

        reserve_coverage_months = data["cash_reserve"] / total_monthly_obligations
        
        return {
            "reserve_coverage_months": reserve_coverage_months
        }


