from calculation_metrics.monthly_annuity_metric import MonthlyAnnuityMetric
from calculation_metrics.residual_income_metric import ResidualIncomeAfterLoanMetric
from calculation_metrics.total_dti_metric import TotalDtiMetric

class CalculationService:
    

    def __init__(self):
        print ("created calculation Metrics")


        self.metrics_registry = {
            "monthly_annuity": MonthlyAnnuityMetric(),
            "total_dti": TotalDtiMetric(),
            "residual_income_after_loan": ResidualIncomeAfterLoanMetric()
        }


    def start(self, REQUIRED_METRICS, APPLICANT_DATA, LEVELS):
        data = APPLICANT_DATA.copy()
        results = {}

        for x in reversed(LEVELS):
            for y in x:

                metrics = self.metrics_registry[y].calculate(data)
                data.update(metrics)

                for ri in REQUIRED_METRICS:
                    
                    if (y == ri):
                        results.update(metrics) # nur wenn metrics augefragt wurde über RequiredInputs wird es als result mitgegeben.

        return results


    def required_inputs(self, metrics: list[str]) -> list[str]:
        required_inputs = []

        for m in metrics:
            if m not in self.metrics_registry:
                raise ValueError(f"Unknown metric: {m}")

            metric = self.metrics_registry[m]

            for required_input in metric.REQUIRED_INPUTS:
                if required_input not in required_inputs:
                    required_inputs.append(required_input)

            dependency_inputs = self.required_inputs(metric.REQUIRED_METRICS)

            for dependency_input in dependency_inputs:
                if dependency_input not in required_inputs:
                    required_inputs.append(dependency_input)

        return required_inputs

#CalculationMetrics => CalculationService
# because later Interface



#Future idea:
#CalculationService could prepare and validate the full metric dependency plan before calculation:
#- resolve required metrics
#- collect required inputs
#- detect missing inputs
#- detect circular metric dependencies
#- determine calculation order
#- execute metrics in order