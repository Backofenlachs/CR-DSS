# model.py
# Annuity Model reines domain-value-object

from dataclasses import dataclass 



@dataclass(frozen=True)
class AnnuityInput:
    principal: float        # K_0
    interest_rate: float    # i (zb. 0.05 für 5%)
    periods: int            # n

    def __post_init__(self):
        if self.principal <= 0:
            raise ValueError("Principal must be positive.")
        if self.periods <= 0:
            raise ValueError("Periods must be positive.")
        if self.interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")