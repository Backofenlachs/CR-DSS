"""
base.py

Enthält die Architektur-Bausteine für das Strategy Pattern
zur Annuitätenberechnung.

Rollen:
- AnnuityCalculationStrategy → Interface 
- AnnuityCalculator → Context 

Die konkrete Implementierung (z.B. StandardAnnuityStrategy)
liegt in separaten Modulen.
"""

from abc import ABC, abstractmethod
from .model import AnnuityInput



class AnnuityCalculationStrategy(ABC):
    """
    Interface  für alle Annuitäten-Algorithmen.

    Jede konkrete Strategie MUSS die Methode `calculate`
    implementieren.

    Vergleich C#:
        public interface IAnnuityCalculationStrategy
    """

    @abstractmethod
    def calculate(self, input_data: AnnuityInput) -> float:
        """
        Führt die eigentliche Annuitätenberechnung durch.

        Muss von jeder konkreten Strategie implementiert werden.
        """
        pass


class AnnuityCalculator:
    """
    Context des Strategy Patterns.

    Diese Klasse kennt nur das Interface,
    nicht die konkrete Implementierung.

    Vergleich C#:
        public class AnnuityCalculator
    """

    def __init__(self, strategy: AnnuityCalculationStrategy):
        # Dependency Injection der Strategie
        self._strategy = strategy

    def calculate(self, input_data: AnnuityInput) -> float:
        """
        Delegiert die Berechnung an die gewählte Strategie.
        """
        return self._strategy.calculate(input_data)
