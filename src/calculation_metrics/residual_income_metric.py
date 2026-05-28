class ResidualIncomeAfterLoanMetric:

    OUTPUT_KEYS = "residual_income_after_loan"

    REQUIRED_INPUTS = [
        "monthly_net_income",
        "monthly_fixed_costs",
        "existing_monthly_debt_payments",
    ]

    REQUIRED_METRICS = [
        "monthly_annuity"
    ]

    def calculate(self, data):

        residual_income_after_loan = (
            data["monthly_net_income"]
            - data["monthly_fixed_costs"]
            - data["existing_monthly_debt_payments"]
            - data["monthly_annuity"]
        )

        return {
            "residual_income_after_loan":
                residual_income_after_loan
        }