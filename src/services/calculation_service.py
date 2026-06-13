from calculation_metrics.calculation_metric import CalculationMetric
from calculation_metrics.monthly_annuity_metric import MonthlyAnnuityMetric
from calculation_metrics.residual_income_metric import ResidualIncomeAfterLoanMetric
from calculation_metrics.total_dti_metric import TotalDtiMetric
from calculation_metrics.reserve_coverage_months_metric import ReserveCoverageMonthsMetric

class CalculationService:
    
    def __init__(self):
        print ("create calculation Metrics")


        self.metrics_registry: dict[str, CalculationMetric] = {
            "monthly_annuity": MonthlyAnnuityMetric(),
            "total_dti": TotalDtiMetric(),
            "residual_income_after_loan": ResidualIncomeAfterLoanMetric(),
            "reserve_coverage_months": ReserveCoverageMonthsMetric()
        }


    def start(self, output_metrics: list[str], APPLICANT_DATA: dict, CALCULATION_PLAN: list[list[str]]) -> dict:
        data = APPLICANT_DATA.copy()
        results = {}

        for level in CALCULATION_PLAN:
            for metric_name in level:                
                metric_result = self.metrics_registry[metric_name].calculate(data)
                
                data.update(metric_result) # Wichtig für alle berechnungsergebnisse speichern
                
                if metric_name in output_metrics:
                    results.update(metric_result) # nur wenn metrics angefragt wurde über RequiredMetrics wird es als result mitgegeben.
                        

        return results

#CalculationMetrics => CalculationService
# later Interface for metrics

