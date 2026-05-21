import json
import random

from sextant_mvp.core.graph_engine import GraphEngine
from sextant_mvp.experiments.baseline import BaselineSimulator
from sextant_mvp.core.cascade_engine import CascadeEngine
from sextant_mvp.core.routing_engine import RoutingEngine
from sextant_mvp.core.metrics import Metrics


class ExperimentRunner:
    def __init__(self):
        self.baseline = BaselineSimulator()
        self.metrics = Metrics()

    def load(self, path):
        with open(path, "r") as f:
            return json.load(f)

    def build_graph(self, scenario):
        g = GraphEngine()

        for node in scenario["nodes"]:
            g.add_node(node["id"], node["failure_prob"])

        for edge in scenario["edges"]:
            g.add_edge(edge[0], edge[1])

        return g

    def run_single(self, scenario_path):
        scenario = self.load(scenario_path)
        graph = self.build_graph(scenario)

        # baseline
        baseline_result = self.baseline.run(graph)

        # cascade
        cascade_engine = CascadeEngine(graph)

        initial_failures = set()
        for node in graph.nodes():
            if random.random() < graph.get_failure_prob(node):
                initial_failures.add(node)

        cascade_result = cascade_engine.run(initial_failures)

        # routing
        routing_engine = RoutingEngine(graph)
        start_node = scenario["nodes"][0]["id"]
        routing_result = routing_engine.choose_best_path(start_node)

        # metrics
        total_nodes = len(graph.nodes())

        return {
            "scenario": scenario_path,
            "baseline": baseline_result,
            "cascade": cascade_result,
            "routing": routing_result,
            "metrics": {
                "baseline_score": self.metrics.baseline_score(baseline_result),
                "cascade_impact": self.metrics.cascade_impact(cascade_result, total_nodes),
                "improvement": self.metrics.improvement(
                    self.metrics.baseline_score(baseline_result),
                    self.metrics.cascade_impact(cascade_result, total_nodes)
                )
            }
        }

    def run_all(self, scenario_list):
        results = []

        for s in scenario_list:
            results.append(self.run_single(s))

        return results
