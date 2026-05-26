class ResidualIncomeAfterLoanMetric:

    REQUIRED_INPUTS = [
        "monthly_net_income",
        "monthly_fixed_costs",
        "existing_monthly_debt_payments",
    ]

    REQUIRED_METRICS = [
        "monthly_annuity"
    ]

    def calculate(self, monthly_net_income, monthly_fixed_costs, existing_monthly_debt_payments, monthly_annuity) -> float:
        return monthly_net_income - monthly_fixed_costs - existing_monthly_debt_payments - monthly_annuity
