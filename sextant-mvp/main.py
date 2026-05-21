import json

from sextant_mvp.core.graph_engine import GraphEngine
from sextant_mvp.experiments.baseline import BaselineSimulator


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

    baseline = BaselineSimulator()
    result = baseline.run(graph)

    print("\nBASELINE RESULT:")
    print(result)
