
from CalculationService import CalculationService
from IOHandler import IOHandler 
from ScoringModel import ScoringModel
from scoring_metrics.scoring_metrics_v0_2_0 import ScoringModel2
from MetricDependencyResolver import MetricDependencyResolver

if __name__ == "__main__":
    # Services
    io = IOHandler()
    calc = CalculationService()
    score = ScoringModel2()
    dm = MetricDependencyResolver()


    # read Input
    APPLICANT_DATA = io.json_IO_read('src/loan-request.json');  

    # resolve Metric Dependencies
    DEPENDENCY_PLAN = dm.planLevels(score.REQUIRED_METRICS, calc.metrics_registry)

    allInputs = DEPENDENCY_PLAN['required_inputs'] + score.REQUIRED_INPUTS
    # validate inputs
    io.validate_required_inputs(allInputs, APPLICANT_DATA)
    

    # calculations
    CALCULATION_RESULT = calc.start(score.REQUIRED_METRICS, APPLICANT_DATA, DEPENDENCY_PLAN['calculation_plan'])

    #print(f"CalculationResults: {CALCULATION_RESULT}")

    # all scoring data that scoring model2 needs
    ScoringData = CALCULATION_RESULT.copy()
    for ri in score.REQUIRED_INPUTS:
        ScoringData[ri] = APPLICANT_DATA[ri]

    #print(ScoringData)
    # Scoring
    SCORE_RESULT = score.evaluate(ScoringData)


    ## OutputData
    applicant_result = {
        "applicant_number": APPLICANT_DATA["application_number"],
        "result": SCORE_RESULT,
    }

    # Write Output
    io.json_IO_write('loan-result.json', applicant_result)
    print(f"Risk Assessment Descision: {SCORE_RESULT}")    