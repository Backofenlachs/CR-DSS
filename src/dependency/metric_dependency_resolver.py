from dataclasses import dataclass, field

@dataclass(frozen=True)
class LevelPlan:
    calculation_plan: list[list[str]] # level n -> level 0
    required_inputs: list[str]
    processed_metrics: dict[str, int]

@dataclass(frozen=True)
class MetricDependencyPlan(LevelPlan): 
    scoring_required_inputs: list[str] # level 0 -> level n
    scoring_required_metrics: list[str]

class MetricDependencyResolver:

    def buildDependencyPlan(self, required_data, metrics_registry) -> MetricDependencyPlan:
        required_inputs = []
        required_metrics = []
        
        # trennen von metrics und inputs
        for data_name in required_data:
            if data_name in metrics_registry:
                required_metrics.append(data_name)
            else:
                required_inputs.append(data_name)

        # resolve metrics dependencies

        levels :LevelPlan = self.planLevels(required_metrics, metrics_registry)
        
        return MetricDependencyPlan(
            calculation_plan = list(reversed(levels.calculation_plan)),
            required_inputs = required_inputs + levels.required_inputs,
            processed_metrics = levels.processed_metrics,
            scoring_required_inputs= required_inputs,
            scoring_required_metrics= required_metrics
        )

    def planLevels(self, required_metrics :list[str], metrics_registry) -> LevelPlan:
        levels = [required_metrics]
        processed_metrics = {metric: 0 for metric in required_metrics}
        required_inputs = []

        lvl_index = 0
        has_next_lvl = True

        while has_next_lvl:
            has_next_lvl = False

            current_level = levels[lvl_index]
            next_level = []

            for metric_name in current_level:
                metric = metrics_registry[metric_name]

                for input_name in metric.REQUIRED_INPUTS:
                    if input_name not in required_inputs:
                        required_inputs.append(input_name)

                for dependency in metric.REQUIRED_METRICS:

                    if dependency == metric_name:
                        raise ValueError(
                            f"kreis Abhängigkeit erkannt: {metric_name} hängt von sich selbst ab"
                        )

                    new_level = lvl_index + 1

                    if dependency not in processed_metrics:
                        next_level.append(dependency)
                        processed_metrics[dependency] = new_level
                        has_next_lvl = True

                    else:
                        existing_level = processed_metrics[dependency]

                        if new_level > existing_level:
                            levels[existing_level].remove(dependency)
                            next_level.append(dependency)
                            processed_metrics[dependency] = new_level
                            has_next_lvl = True

            if next_level:
                levels.append(next_level)

            lvl_index += 1

        return LevelPlan(
            calculation_plan = levels,
            required_inputs = required_inputs,
            processed_metrics = processed_metrics
        )