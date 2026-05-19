#applicant.py

from dataclasses import dataclass



@dataclass
class Applicant:
    name: str
    age: int
    monthly_income: float
    fixed_costs: float
    existing_loans: float
    employment_years: int