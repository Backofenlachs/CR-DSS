from abc import ABC, abstractmethod

class CalculationMetric(ABC):
    NAME : str | None= None
    REQUIRED_INPUTS : list[str]= []
    REQUIRED_OUTPUTS : list[str]= []
    OUTPUT_KEYS : list[str]= []

    
    def calculate(self, data: dict) -> dict[str, float]:
        self._validate_metric_contract()
        self._validate_required_data(data)
        result = self._calculate(data)
        self._validate_outputkeys(result)
        return result
        

    @abstractmethod
    def _calculate(self, data) -> dict[str, float]: 
        pass



    def _validate_required_data(self, data) -> None:
        required_data = (
            set(self.REQUIRED_INPUTS) | set(self.REQUIRED_INPUTS)
        )

        missing_data = required_data - set(data.keys())

        if missing_data: 
            raise ValueError(
                f"[{self.NAME}] Missing required data: {sorted(missing_data)}"
            )

    def _validate_outputkeys(self, result) -> None:
        required_keys = set(self.OUTPUT_KEYS)
        actual_keys = set(result.keys())

        missing_keys = required_keys - actual_keys

        if missing_keys:
            raise ValueError(
                f"[{self.NAME}] Missing output keys: {sorted(missing_keys)}"
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