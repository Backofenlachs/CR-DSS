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
        self._validate_domain_rules(data)

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
    
    #### Ege Cases ####
    MIN_LOAN_AMOUNT = 500
    MAX_LOAN_AMOUNT = 1000000
    MIN_LOAN_TERM_MONTHS = 1
    MAX_LOAN_TERM_MONTHS = 120

    def _validate_domain_rules(self, data):
        loan_amount = data["loan_amount"]
        annual_interest_rate = data["annual_interest_rate"]
        loan_term_months = data["loan_term_months"]

        if not isinstance(loan_amount, int):
            raise ValueError("loan_amount must be an integer")

        if not isinstance(annual_interest_rate, (int, float)):
            raise ValueError("annual_interest_rate must be numeric")

        if not isinstance(loan_term_months, int):
            raise ValueError("loan_term_months must be an integer")


        if annual_interest_rate < 0:
            raise ValueError("annual_interest_rate must not be negative")

        if loan_amount < self.MIN_LOAN_AMOUNT:
            raise ValueError(f"loan_amount must be at least {self.MIN_LOAN_AMOUNT} ")
        
        if loan_amount > self.MAX_LOAN_AMOUNT:
            raise ValueError(f"loan_amount must not exceed {self.MAX_LOAN_AMOUNT}")
        
        if loan_term_months < self.MIN_LOAN_TERM_MONTHS:
            raise ValueError(f"loan_term_months must be at least {self.MIN_LOAN_TERM_MONTHS}")
        
        if loan_term_months > self.MAX_LOAN_TERM_MONTHS:
            raise ValueError(f"loan_term_months must not exceed {self.MAX_LOAN_TERM_MONTHS}")
