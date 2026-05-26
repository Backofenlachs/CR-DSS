class MonthlyAnnuityMetric:
    
    REQUIRED_INPUTS = [
        "loan_amount",
        "interest_rate",
        "periods"
    ]

    REQUIRED_METRICS = []

    def calculate(self, loan_amount, interest_rate, periods) -> dict[str, float]:
        K0 = loan_amount
        i = interest_rate
        n = periods

        if i == 0:
            monthly_payment = K0 / n
        else:
            numerator = i * (1 + i) ** n
            denominator = (1 + i) ** n - 1
            monthly_payment = K0 * (numerator / denominator)

        
        
        total_payment = monthly_payment * n
        total_interest = total_payment - K0

        return {
            "monthly_payment": monthly_payment,
            "total_payment": total_payment,
            "total_interest": total_interest
        }