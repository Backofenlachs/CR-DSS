import pytest

from calculation_metrics.calculation_metric import CalculationMetric


class ValidDummyMetric(CalculationMetric):
    NAME = "dummy_result"

    REQUIRED_INPUTS = [
        "input_a"
    ]

    REQUIRED_METRICS = [
        "metric_b"
    ]

    OUTPUT_KEYS = [
        "dummy_result"
    ]

    def _calculate(self, data):
        return {
            "dummy_result": data["input_a"] + data["metric_b"]
        }


class MissingNameMetric(CalculationMetric):
    REQUIRED_INPUTS = []

    REQUIRED_METRICS = []

    OUTPUT_KEYS = [
        "result"
    ]

    def _calculate(self, data):
        return {
            "result": 1
        }


class EmptyOutputKeysMetric(CalculationMetric):
    NAME = "result"

    REQUIRED_INPUTS = []

    REQUIRED_METRICS = []

    OUTPUT_KEYS = []

    def _calculate(self, data):
        return {
            "result": 1
        }


class NameOutputMismatchMetric(CalculationMetric):
    NAME = "wrong_name"

    REQUIRED_INPUTS = []

    REQUIRED_METRICS = []

    OUTPUT_KEYS = [
        "result"
    ]

    def _calculate(self, data):
        return {
            "result": 1
        }


class MissingOutputKeyMetric(CalculationMetric):
    NAME = "expected_result"

    REQUIRED_INPUTS = []

    REQUIRED_METRICS = []

    OUTPUT_KEYS = [
        "expected_result"
    ]

    def _calculate(self, data):
        return {
            "wrong_result": 1
        }


def test_valid_metric_works():
    metric = ValidDummyMetric()

    result = metric.calculate({
        "input_a": 10,
        "metric_b": 5
    })

    assert result == {
        "dummy_result": 15
    }


def test_missing_required_input_fails():
    metric = ValidDummyMetric()

    with pytest.raises(ValueError, match="Missing required data"):
        metric.calculate({
            "metric_b": 5
        })


def test_missing_required_metric_fails():
    metric = ValidDummyMetric()

    with pytest.raises(ValueError, match="Missing required data"):
        metric.calculate({
            "input_a": 10
        })


def test_missing_name_fails():
    with pytest.raises(NotImplementedError, match="must define NAME"):
        MissingNameMetric()


def test_empty_output_keys_fails():
    with pytest.raises(NotImplementedError, match="OUTPUT_KEYS must not be empty"):
        EmptyOutputKeysMetric()


def test_name_output_mismatch_fails():
    with pytest.raises(ValueError, match="NAME should match first OUTPUT_KEY"):
        NameOutputMismatchMetric()


def test_missing_output_key_fails():
    metric = MissingOutputKeyMetric()

    with pytest.raises(ValueError, match="Invalid output keys"):
        metric.calculate({})