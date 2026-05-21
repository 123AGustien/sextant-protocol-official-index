class Metrics:
    def baseline_score(self, baseline_result):
        return round(baseline_result["success_rate"], 3)

    def cascade_impact(self, cascade_result, total_nodes):
        failed = len(cascade_result["failed_nodes"])
        return round(failed / total_nodes, 3)

    def improvement(self, baseline_score, cascade_impact):
        return round(baseline_score - cascade_impact, 3)
