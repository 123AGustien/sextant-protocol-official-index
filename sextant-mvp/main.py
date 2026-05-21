import json
import random

from sextant_mvp.core.graph_engine import GraphEngine
from sextant_mvp.experiments.baseline import BaselineSimulator
from sextant_mvp.core.cascade_engine import CascadeEngine


def load_scenario(path):
    with open(path, "r") as f:
        return json.load(f)


def build_graph(scenario):
    g = GraphEngine()

    for node in scenario["nodes"]:
        g.add_node(node["id"], node["failure_prob"])

    for edge in scenario["edges"]:
        g.add_edge(edge[0], edge[1])

    return g


if __name__ == "__main__":
    scenario = load_scenario("sextant-mvp/scenarios/sample_workflow.json")

    graph = build_graph(scenario)

    # -------------------------
    # BASELINE RUN
    # -------------------------
    baseline = BaselineSimulator()
    baseline_result = baseline.run(graph)

    print("\nBASELINE RESULT:")
    print(baseline_result)

    # -------------------------
    # CASCADE RUN
    # -------------------------
    cascade_engine = CascadeEngine(graph)

    initial_failures = set()

    for node in graph.nodes():
        if random.random() < graph.get_failure_prob(node):
            initial_failures.add(node)

    cascade_result = cascade_engine.run(initial_failures)

    print("\nCASCADE RESULT:")
    print(cascade_result)
