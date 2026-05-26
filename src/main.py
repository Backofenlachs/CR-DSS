
from CalculationService import CalculationService
from IOHandler import IOHandler 
from ScoringModel import ScoringModel


if "__main__" == "__main__":
    # Services
    io = IOHandler()
    calc = CalculationService()
    score = ScoringModel()

    print(calc.required_inputs(score.REQUIRED_METRICS))

    # read Input
    applicant_data = io.json_IO_read('src/loan-request.json');  

    # calculations
    annuity_calculation_results = calc.calculate(applicant_data["loan_amount"], applicant_data["annual_interest_rate"]/12, applicant_data["terms_in_months"])
    total_dti = calc.calculate_total_dti(applicant_data["monthly_net_income"], annuity_calculation_results["monthly_payment"], applicant_data["existing_monthly_dept_payments"])
    residual_income_after_loan = calc.calculate_resuidal_income_after_loan(applicant_data["monthly_net_income"], applicant_data["monthly_fixed_costs"], applicant_data["existing_monthly_dept_payments"], annuity_calculation_results["monthly_payment"])

    scoring_result = score.evaluate(total_dti, residual_income_after_loan)


    ## OutputData
    applicant_result = {
        "applicant_number": applicant_data["application_number"],
        "result": scoring_result
    }

    # Write Output
    io.json_IO_write('loan-result.json', applicant_result)
    print(f"Risk Assesment Descision: {scoring_result}")    