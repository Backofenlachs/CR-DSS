#test_applicant.py

import pytest
from domain.applicant import Applicant



def test_applicant_creation():
    applicant = Applicant(
        name="John Doe",
        age=30,
        monthly_income=5000.0,
        fixed_costs=1500.0,
        existing_loans=20000.0,
        employment_years=5
    )
    assert applicant.name == "John Doe"
    assert applicant.age == 30
    assert applicant.monthly_income == 5000.0
    assert applicant.fixed_costs == 1500.0
    assert applicant.existing_loans == 20000.0
    assert applicant.employment_years == 5