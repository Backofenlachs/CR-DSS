from domain.annuity_models import AnnuityParameters
from domain.annuity_standart_strategy import AnnuityStandardStrategy


def test_annuity_basic():
    strategy = AnnuityStandardStrategy()

    params = AnnuityParameters(
        principal=10000.0,
        interest_rate=0.05,
        periods=36
    )

    result = strategy.calculate(params)

    assert result.monthly_payment > 0
    assert result.total_payment > 10000.0
    assert result.total_interest > 0