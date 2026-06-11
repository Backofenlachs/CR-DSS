from calculation_metrics.monthly_annuity_metric import MonthlyAnnuityMetric
from calculation_metrics.residual_income_metric import ResidualIncomeAfterLoanMetric
from calculation_metrics.total_dti_metric import TotalDtiMetric
from calculation_metrics.reserve_coverage_months_metric import ReserveCoverageMonthsMetric

class CalculationService:
    

    def __init__(self):
        print ("created calculation Metrics")


        self.metrics_registry = {
            "monthly_annuity": MonthlyAnnuityMetric(),
            "total_dti": TotalDtiMetric(),
            "residual_income_after_loan": ResidualIncomeAfterLoanMetric(),
            "reserve_coverage_months": ReserveCoverageMonthsMetric()
        }


    def start(self, REQUIRED_METRICS, APPLICANT_DATA, CALCULATION_PLAN):
        data = APPLICANT_DATA.copy()
        results = {}

        for level in CALCULATION_PLAN:
            for metrics_name in level:

                metrics = self.metrics_registry[metrics_name].calculate(data)
                data.update(metrics)

                for ri in REQUIRED_METRICS:
                    
                    if (metrics_name == ri):
                        results.update(metrics) # nur wenn metrics angefragt wurde über RequiredInputs wird es als result mitgegeben.

        return results

#CalculationMetrics => CalculationService
# later Interface for metrics



#Future idea:
#CalculationService could prepare and validate the full metric dependency plan before calculation:
#- resolve required metrics
#- collect required inputs
#- detect missing inputs
#- detect circular metric dependencies
#- determine calculation order
#- execute metrics in order