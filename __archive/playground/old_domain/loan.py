#loan.py

from dataclasses import dataclass



@dataclass
class Loan:
    principal: float
    interest_rate: float
    duration_months: int