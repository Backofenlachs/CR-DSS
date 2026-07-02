from abc import ABC, abstractmethod
from typing import Any


class CalculationMetric(ABC):
    NAME: str | None = None
    REQUIRED_INPUTS: list[str] = []
    REQUIRED_METRICS: list[str] = []
    OUTPUT_KEYS: list[str] = []

    def __init__(self) -> None:
        self._validate_metric_contract()

    def calculate(self, data: dict[str, Any]) -> dict[str, float]:
        self._validate_required_data(data)

        result = self._calculate(data)

        self._validate_outputkeys(result)

        return result

    @abstractmethod
    def _calculate(self, data: dict[str, Any]) -> dict[str, float]:
        pass

    def _validate_required_data(self, data: dict[str, Any]) -> None:
        required_data = (
            set(self.REQUIRED_INPUTS) | set(self.REQUIRED_METRICS)
        )

        missing_data = required_data - set(data.keys())

        if missing_data:
            raise ValueError(
                f"[{self.NAME}] Missing required data: {sorted(missing_data)}"
            )

    def _validate_outputkeys(self, result: dict[str, float]) -> None:
        required_keys = set(self.OUTPUT_KEYS)
        actual_keys = set(result.keys())

        if required_keys != actual_keys:
            raise ValueError(
                f"[{self.NAME}] Invalid output keys. "
                f"Expected {sorted(required_keys)}, got {sorted(actual_keys)}"
            )

    def _validate_metric_contract(self) -> None:
        if self.NAME is None:
            raise NotImplementedError(
                f"{self.__class__.__name__} must define NAME"
            )

        if not self.OUTPUT_KEYS:
            raise NotImplementedError(
                f"[{self.NAME}] OUTPUT_KEYS must not be empty"
            )

        if self.NAME != self.OUTPUT_KEYS[0]:
            raise ValueError(
                f"[{self.NAME}] NAME should match first OUTPUT_KEY "
                f"('{self.OUTPUT_KEYS[0]}')"
            )