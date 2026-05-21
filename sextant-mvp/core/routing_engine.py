import random

class RoutingEngine:
    def __init__(self, graph_engine):
        self.graph = graph_engine.graph

    def simulate_path_risk(self, start_node, steps=3):
        """
        Simulates risk along a random path starting from a node.
        """

        current = start_node
        total_risk = 0.0

        for _ in range(steps):
            neighbors = list(self.graph.successors(current))

            if not neighbors:
                break

            next_node = random.choice(neighbors)

            node_risk = self.graph.nodes[next_node]["failure_prob"]

            total_risk += node_risk

            current = next_node

        return total_risk

    def choose_best_path(self, start_node, trials=5):
        """
        Simulates multiple futures and picks lowest-risk path.
        """

        best_risk = float("inf")
        best_score = None

        for _ in range(trials):
            risk = self.simulate_path_risk(start_node)

            if risk < best_risk:
                best_risk = risk
                best_score = risk

        return {
            "best_risk_score": round(best_score, 3),
            "trials": trials
        }
