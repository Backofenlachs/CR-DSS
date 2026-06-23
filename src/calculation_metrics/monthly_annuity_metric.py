from calculation_metrics.calculation_metric import CalculationMetric

class MonthlyAnnuityMetric(CalculationMetric):
    NAME = "monthly_annuity"

    OUTPUT_KEYS = [
        "monthly_annuity",
        "total_repayment",
        "total_interest"
    ]

    REQUIRED_INPUTS = [
        "loan_amount",
        "annual_interest_rate",
        "loan_term_months"
    ]

    REQUIRED_METRICS = []

    def _calculate(self, data):
        K0 = data['loan_amount']
        i = data['annual_interest_rate'] / 12
        n = data['loan_term_months']

        if i == 0:
            monthly_payment = K0 / n
        else:
            term =  (1 + i) ** n
            monthly_payment = K0 * ((i * term)  / (term - 1))

        
        
        total_payment = monthly_payment * n
        total_interest = total_payment - K0

        return {
            "monthly_annuity": monthly_payment,
            "total_repayment": total_payment,
            "total_interest": total_interest
        }