"""
Unit Tests für das Annuitäten-Modul.
"""

import pytest

from domain.annuity.base import AnnuityCalculator
from domain.annuity.model import AnnuityInput
from domain.annuity.standard import StandardAnnuityStrategy

# ---------------------------------------------------------
# Happy Path
# ---------------------------------------------------------

def test_annuity_basic_case():
    """
    100.000 €
    5 % Zins
    10 Jahre

    Erwartete Annuität ≈ 12.950,46 €
    """

    data = AnnuityInput(
        principal=100_000,
        interest_rate=0.05,
        periods=10
    )

    calculator = AnnuityCalculator(StandardAnnuityStrategy())
    result = calculator.calculate(data)

    assert round(result, 2) == 12950.46


# ---------------------------------------------------------
# Edge Case: Nullzins
# ---------------------------------------------------------

def test_zero_interest_rate():
    """
    Bei 0 % Zins ist die Annuität einfach
    Kreditbetrag / Laufzeit.
    """

    data = AnnuityInput(
        principal=100_000,
        interest_rate=0.0,
        periods=10
    )

    calculator = AnnuityCalculator(StandardAnnuityStrategy())
    result = calculator.calculate(data)

    assert result == 10_000


# ---------------------------------------------------------
# Validierungsfälle
# ---------------------------------------------------------

def test_invalid_principal():
    with pytest.raises(ValueError):
        AnnuityInput(
            principal=-100_000,
            interest_rate=0.05,
            periods=10
        )


def test_invalid_interest_rate():
    with pytest.raises(ValueError):
        AnnuityInput(
            principal=100_000,
            interest_rate=-0.01,
            periods=10
        )


def test_invalid_periods():
    with pytest.raises(ValueError):
        AnnuityInput(
            principal=100_000,
            interest_rate=0.05,
            periods=0
        )
