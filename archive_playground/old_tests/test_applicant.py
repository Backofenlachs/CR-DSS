#test_applicant.py

import pytest
from domain.applicant import Applicant

test_name="John Doe"
test_age=30
test_monthly_income=5000
test_fixed_costs=1500
test_existing_loans=20000
test_employment_years=5


def test_applicant_creation():
    applicant = Applicant(
        name=test_name,
        age=test_age,
        monthly_income=test_monthly_income,
        fixed_costs=test_fixed_costs,
        existing_loans=test_existing_loans,
        employment_years=test_employment_years
    )
    assert applicant.name == test_name
    assert applicant.age == test_age
    assert applicant.monthly_income == test_monthly_income
    assert applicant.fixed_costs == test_fixed_costs
    assert applicant.existing_loans == test_existing_loans
    assert applicant.employment_years == test_employment_years