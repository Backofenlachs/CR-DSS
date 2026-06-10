from reserve_coverage_months_metric import ReserveCoverageMonthsMetric

def main():

    metric = ReserveCoverageMonthsMetric()

    data = {
        "monthly_fixed_costs": 1000,
        "existing_monthly_debt_payments": 200,
        "monthly_annuity": 300,
        "cash_reserve": 9000
    }

    result = metric.calculate(data)

    print("Result:")
    print(result)

    expected = 9000 / (1000 + 200 + 300)

    print(f"Expected: {expected}")
    print(f"Actual:   {result['reserve_coverage_months']}")

    assert abs(
        result["reserve_coverage_months"] - expected
    ) < 0.0001

    print("Test passed.")


if __name__ == "__main__":
    main()