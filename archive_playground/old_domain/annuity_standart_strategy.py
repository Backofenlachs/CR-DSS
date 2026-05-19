from .annuity_models import AnnuityParameters, AnnuityResult
from .annuity_strategy import IAnnuityCalculationStrategy


class AnnuityStandardStrategy(IAnnuityCalculationStrategy):
    """
    Formel:

        A = K0 * [ i(1+i)^n ] / [ (1+i)^n - 1 ]
    """

    def calculate(self, p: AnnuityParameters) -> AnnuityResult:
        K0 = p.principal
        i = p.interest_rate
        n = p.periods

        if i == 0:
            monthly_payment = K0 / n
        else:
            numerator = i * (1 + i) ** n
            denominator = (1 + i) ** n - 1
            monthly_payment = K0 * (numerator / denominator)

        total_payment = monthly_payment * n
        total_interest = total_payment - K0

        return AnnuityResult(
            monthly_payment=monthly_payment,
            total_payment=total_payment,
            total_interest=total_interest,
        )