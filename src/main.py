
from CalculationService import CalculationService
from IOHandler import IOHandler 
from ScoringModel import ScoringModel
from MetricDependencyResolver import MetricDependencyResolver

if "__main__" == "__main__":
    # Services
    io = IOHandler()
    calc = CalculationService()
    score = ScoringModel()
    dm = MetricDependencyResolver()


    # read Input
    APPLICANT_DATA = io.json_IO_read('src/loan-request.json');  

    # resolve Metric Dependencies
    DEPENDENCY_PLAN = dm.planLevels(score.REQUIRED_METRICS, calc.metrics_registry)

    # validate inputs
    io.validate_required_inputs(DEPENDENCY_PLAN['required_inputs'], APPLICANT_DATA)
    
    # calculations
    CALCULATION_RESULT = calc.start(score.REQUIRED_METRICS, APPLICANT_DATA, DEPENDENCY_PLAN['calculation_plan'])

    # Scoring
    SCORE_RESULT = score.evaluate(CALCULATION_RESULT)


    ## OutputData
    applicant_result = {
        "applicant_number": APPLICANT_DATA["application_number"],
        "result": SCORE_RESULT,
    }

    # Write Output
    io.json_IO_write('loan-result.json', applicant_result)
    print(f"Risk Assessment Descision: {SCORE_RESULT}")    