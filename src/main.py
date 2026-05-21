import os
import json

def calculate(loan_amount, interest_rate, periods) -> object:
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

def json_IO_read() -> dict:
    with open('src/loan-request.json', 'r', encoding='utf-8') as file:
        data_dict = json.load(file)

    return data_dict

def json_IO_write(data):
    with open('loan-result.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def calculate_total_dti(monthly_net_income, new_monthly_annuity, existing_monthly_debt_payments ) -> float:
    total_monthly_debt_payments = existing_monthly_debt_payments + new_monthly_annuity

    return (total_monthly_debt_payments / monthly_net_income)

def calculate_resuidal_income_after_loan(monthly_net_income, monthly_fixed_costs, existing_monthly_debt_payments, monthly_annuity) -> float:
    return monthly_net_income - monthly_fixed_costs - existing_monthly_debt_payments - monthly_annuity

def scoring_model(total_dti, residual_income_after_loan) -> str:
    
    ## results
    
    if (total_dti <= 0.35 and residual_income_after_loan >= 500):
        return "APPROVED"
    elif (total_dti <= 0.45 and residual_income_after_loan >= 250):
        return "REVIEW"
    else:
        return "DECLINED"


if "__main__" == "__main__":
    applicant_data = json_IO_read();
    
    # calculations
    annuity_calculation_results = calculate(applicant_data["loan_amount"], applicant_data["annual_interest_rate"]/12, applicant_data["terms_in_months"])
    ## kennzahlen
    total_dti = calculate_total_dti(applicant_data["monthly_net_income"], annuity_calculation_results[0], applicant_data["existing_monthly_dept_payments"])
    residual_income_after_loan = calculate_resuidal_income_after_loan(applicant_data["monthly_net_income"], applicant_data["monthly_fixed_costs"], applicant_data["existing_monthly_dept_payments"], annuity_calculation_results[0])

    scoring_result = scoring_model(total_dti, residual_income_after_loan)

    ## Map OutputData
    applicant_result = {
        "applicant_number": applicant_data["application_number"],
        "result": scoring_result
    }

    # Write Output
    json_IO_write(applicant_result)
    print(f"Risk Assesment Descision: {scoring_result}")    