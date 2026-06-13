from abc import ABC, abstractmethod

class CalculationMetric(ABC):

    OUTPUT_KEYS : list[str]= []
    REQUIRED_INPUTS : list[str]= []
    REQUIRED_OUTPUTS : list[str]= []

    @abstractmethod
    def calculate(self, data: dict) -> dict[str, float]:
        pass