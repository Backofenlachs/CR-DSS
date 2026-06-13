from scoring_models.scoring_model_v0_1_0 import ScoringModel1
from scoring_models.scoring_model_v0_2_0 import ScoringModel2

class ScoringService:
    SCORING_MODEL_REGISTRY = {
        "v0.1.0": ScoringModel1,
        "v0.2.0": ScoringModel2,
    }

    def __init__(self):
        print("created ScoringService")
        self.activeModel = None

    def select(self, scoring_model_name):
        if scoring_model_name not in self.SCORING_MODEL_REGISTRY:
            raise ValueError(
                f"[ScoringService.select] unknown scoring model: {scoring_model_name}"
            )

        self.activeModel = self.SCORING_MODEL_REGISTRY[scoring_model_name]()

    def getRequiredData(self) ->list[str]:
        if self.activeModel is None:
            raise ValueError(
                "[ScoringService.getRequiredData] no scoring model selected"
            )

        return self.activeModel.REQUIRED_DATA

    def evaluate(self, data) -> str:
        if self.activeModel is None:
            raise ValueError(
                "[ScoringService.evaluate] no scoring model selected"
            )

        return self.activeModel.evaluate(data)