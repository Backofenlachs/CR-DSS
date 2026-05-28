class TotalDtiMetric:

    OUTPUT_KEYS = "total_dti"

    REQUIRED_INPUTS = [
        "monthly_net_income",
        "existing_monthly_debt_payments"
    ]

    REQUIRED_METRICS = [
        "monthly_annuity"
    ]

    def calculate(self, data) -> float:
        total_monthly_debt_payments = data['existing_monthly_debt_payments'] + data['monthly_annuity']

        total_dti = total_monthly_debt_payments / data['monthly_net_income']

        return {
            "total_dti": total_dti
        }