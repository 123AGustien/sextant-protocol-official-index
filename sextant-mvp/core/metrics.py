class Metrics:
    def baseline_score(self, baseline_result, total_nodes):
        return round(baseline_result["success_rate"], 3)

    def cascade_impact(self, cascade_result, total_nodes):
        failed = len(cascade_result["failed_nodes"])
        return round(failed / total_nodes, 3)

    def improvement(self, baseline_score, cascade_impact):
        # lower is better for cascade impact, higher is better for success
        return round(baseline_score - cascade_impact, 3)
