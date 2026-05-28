
from CalculationService import CalculationService
from IOHandler import IOHandler 
from ScoringModel import ScoringModel

def MissingInputError(missing_inputs):
    return print(f"missing inputs: {missing_inputs}")

if "__main__" == "__main__":
    # Services
    io = IOHandler()
    calc = CalculationService()
    score = ScoringModel()


    # read Input
    APPLICANT_DATA = io.json_IO_read('src/loan-request.json');  

    # resolve dependencies
    REQUIRED_INPUTS = calc.required_inputs(score.REQUIRED_METRICS)
    
    # validate inputs
    io.validate_required_inputs(REQUIRED_INPUTS, APPLICANT_DATA)
    
    # calculations
    result = calc.start(APPLICANT_DATA)

    scoring_result = score.evaluate(result['total_dti'], result['residual_income_after_loan'])


    ## OutputData
    applicant_result = {
        "applicant_number": APPLICANT_DATA["application_number"],
        "result": scoring_result
    }

    # Write Output
    io.json_IO_write('loan-result.json', applicant_result)
    print(f"Risk Assesment Descision: {scoring_result}")    