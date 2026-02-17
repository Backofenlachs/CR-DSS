"""
standard.py

Klassische Annuitätenformel mit konstantem Zinssatz.
"""

from .base import AnnuityCalculationStrategy
from .model import AnnuityInput


class StandardAnnuityStrategy(AnnuityCalculationStrategy):
    """
    Formel:

        A = K0 * [ i(1+i)^n ] / [ (1+i)^n - 1 ]
    """

    def calculate(self, input_data: AnnuityInput) -> float:
        K0 = input_data.principal
        i = input_data.interest_rate
        n = input_data.periods

        if i == 0:
            return K0 / n

        numerator = i * (1 + i) ** n
        denominator = (1 + i) ** n - 1

        return K0 * (numerator / denominator)
