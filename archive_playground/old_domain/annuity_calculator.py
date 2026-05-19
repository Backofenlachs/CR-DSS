from .annuity_models import AnnuityParameters, AnnuityResult
from .annuity_strategy import IAnnuityCalculationStrategy

class AnnuityCalculator:
    def __init__(self, strategy: IAnnuityCalculationStrategy):
        self._strategy = strategy

    def calculate(self, params: AnnuityParameters) -> AnnuityResult:
        return self._strategy.calculate(params)