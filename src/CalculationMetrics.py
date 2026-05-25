class CalculationMetrics:

    def __init__(self):
         print ("Created Calculation Metrics")
         pass

    def calculate(self, loan_amount, interest_rate, periods) -> object:
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

            return (
                monthly_payment,
                total_payment,
                total_interest
            )
    

    def calculate_total_dti(self, monthly_net_income, new_monthly_annuity, existing_monthly_debt_payments ) -> float:
        total_monthly_debt_payments = existing_monthly_debt_payments + new_monthly_annuity

        return (total_monthly_debt_payments / monthly_net_income)


    def calculate_resuidal_income_after_loan(self, monthly_net_income, monthly_fixed_costs, existing_monthly_debt_payments, monthly_annuity) -> float:
        return monthly_net_income - monthly_fixed_costs - existing_monthly_debt_payments - monthly_annuity
