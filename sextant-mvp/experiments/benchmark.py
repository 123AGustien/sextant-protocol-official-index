import random

class BenchmarkRunner:
    def __init__(self, graph_engine, baseline, cascade_engine, routing_engine):
        self.graph = graph_engine
        self.baseline = baseline
        self.cascade_engine = cascade_engine
        self.routing_engine = routing_engine

    def run(self, scenario, runs=100):
        baseline_scores = []
        cascade_impacts = []
        routing_scores = []

        nodes = self.graph.nodes()
        total_nodes = len(nodes)

        for _ in range(runs):

            # ---------------- BASELINE ----------------
            baseline_result = self.baseline.run(self.graph)
            baseline_scores.append(baseline_result["success_rate"])

            # ---------------- CASCADE ----------------
            initial_failures = set()

            for node in nodes:
                if random.random() < self.graph.get_failure_prob(node):
                    initial_failures.add(node)

            cascade_result = self.cascade_engine.run(initial_failures)

            cascade_impacts.append(len(cascade_result["failed_nodes"]) / total_nodes)

            # ---------------- ROUTING ----------------
            start_node = nodes[0]
            routing_result = self.routing_engine.choose_best_path(start_node)

            routing_scores.append(routing_result["best_risk_score"])

        return {
            "baseline_avg": round(sum(baseline_scores) / runs, 3),
            "cascade_avg": round(sum(cascade_impacts) / runs, 3),
            "routing_avg_risk": round(sum(routing_scores) / runs, 3),
            "runs": runs
        }
