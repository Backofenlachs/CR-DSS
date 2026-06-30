from calculation_metrics.calculation_metric import CalculationMetric

class TotalDtiMetric(CalculationMetric):

    NAME = "total_dti"

    REQUIRED_INPUTS = [
        "monthly_net_income",
        "existing_monthly_debt_payments"
    ]

    REQUIRED_METRICS = [
        "monthly_annuity"
    ]

    OUTPUT_KEYS = [
        "total_dti"
    ]

    def _calculate(self, data):
        if data["monthly_net_income"] <= 0:
            raise ValueError("monthly_net_income must be greater than 0")
    
        if data["existing_monthly_debt_payments"] < 0:
            raise ValueError("existing_monthly_debt_payments must not be negative")
        
        if data["monthly_annuity"] < 0:
            raise ValueError("monthly_annuity must not be negative")
        

        total_monthly_debt_payments = (
            data['existing_monthly_debt_payments'] 
            + data['monthly_annuity']
        )

        total_dti = total_monthly_debt_payments / data['monthly_net_income']

        return {
            "total_dti": total_dti
        }