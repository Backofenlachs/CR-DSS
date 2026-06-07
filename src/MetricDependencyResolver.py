class MetricDependencyResolver:

    def planLevels(self, requiredMetrics, metricsRegistry):
        levels = [requiredMetrics]
        processed_metrics = {metric: 0 for metric in requiredMetrics}
        required_inputs = []

        lvl_index = 0
        has_next_lvl = True

        while has_next_lvl:
            has_next_lvl = False

            current_level = levels[lvl_index]
            next_level = []

            for metric_name in current_level:
                metric = metricsRegistry[metric_name]

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

        return {
            "levels": levels,
            "required_inputs": required_inputs,
            "processed_metrics": processed_metrics
        }