#test_loan.py

import pytest
from domain.loan import Loan



def test_loan_creation():
    loan = Loan(
        principal=10000.0,
        interest_rate=5.0,
        duration_months=36
    )
    assert loan.principal == 10000.0
    assert loan.interest_rate == 5.0
    assert loan.duration_months == 36