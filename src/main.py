
from services.calculation_service import CalculationService
from services.io_handler import IOHandler 
from services.scoring_service import ScoringService

from dependency.metric_dependency_resolver import MetricDependencyResolver

if __name__ == "__main__":
    # Services
    io = IOHandler()
    calc = CalculationService()
    score = ScoringService()
    dm = MetricDependencyResolver()


    # read Input
    APPLICANT_DATA = io.json_IO_read('data/loan-request.json');  

    # validate and select Scoring Model
    score.select(APPLICANT_DATA["scoring_model"])
    
    
    # resolve Metric Dependencies
    DEPENDENCY_PLAN = dm.buildDependencyPlan(score.getRequiredData(), calc.metrics_registry)
    

    # validate inputs
    io.validate_required_inputs(DEPENDENCY_PLAN.required_inputs, APPLICANT_DATA)
    

    # calculations
    CALCULATION_RESULT = calc.start(DEPENDENCY_PLAN.scoring_required_metrics, APPLICANT_DATA, DEPENDENCY_PLAN.calculation_plan)


    # merge the calculationresults and the needed inputs in scoringData
    ScoringData = CALCULATION_RESULT.copy()
    for required_input in DEPENDENCY_PLAN.scoring_required_inputs:
        ScoringData[required_input] = APPLICANT_DATA[required_input]

    # Scoring
    SCORE_RESULT = score.evaluate(ScoringData)


    ## OutputData
    applicant_result = {
        "applicant_number": APPLICANT_DATA["application_number"],
        "result": SCORE_RESULT,
    }

    # Write Output
    io.json_IO_write('data/loan-result.json', applicant_result)
    print(f"Risk Assessment Decision: {SCORE_RESULT}")    