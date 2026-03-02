from dataclasses import dataclass


@dataclass
class AnnuityParameters:
    """Value Object for annuity calculation."""
    principal: float
    interest_rate: float  # annual nominal rate, e.g. 0.05 for 5%
    periods: int          # number of months


@dataclass
class AnnuityResult:
    """Value Object for annuity calculation result."""
    monthly_payment: float
    total_payment: float
    total_interest: float