
from abc import ABC, abstractmethod

from .annuity_models import AnnuityParameters, AnnuityResult

class IAnnuityCalculationStrategy(ABC):
    @abstractmethod
    def calculate(self, p: AnnuityParameters) -> AnnuityResult:
        """Calculate annuity result for given parameters"""
        raise NotImplementedError