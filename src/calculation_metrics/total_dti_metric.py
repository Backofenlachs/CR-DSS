class TotalDtiMetric:

    REQUIRED_INPUTS = [
        "monthly_net_income",
        "existing_monthly_debt_payments"
    ]

    REQUIRED_METRICS = [
        "monthly_annuity"
    ]

    def calculate(self, monthly_net_income, new_monthly_annuity, existing_monthly_debt_payments ) -> float:
        total_monthly_debt_payments = existing_monthly_debt_payments + new_monthly_annuity

        return (total_monthly_debt_payments / monthly_net_income)
