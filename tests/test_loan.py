#test_loan.py

import pytest
from domain.loan import Loan

test_principal=10000
test_interest_rate=5.0
test_duration_months=36

def test_loan_creation():
    loan = Loan(
        principal=test_principal,
        interest_rate=test_interest_rate,
        duration_months=test_duration_months
    )
    assert loan.principal == test_principal
    assert loan.interest_rate == test_interest_rate
    assert loan.duration_months == test_duration_months