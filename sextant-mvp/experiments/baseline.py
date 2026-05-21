import random

class BaselineSimulator:
    def run(self, graph_engine):
        failed_nodes = []

        for node in graph_engine.nodes():
            prob = graph_engine.get_failure_prob(node)

            if random.random() < prob:
                failed_nodes.append(node)

        success_rate = 1 - (len(failed_nodes) / len(graph_engine.nodes()))

        return {
            "failed_nodes": failed_nodes,
            "success_rate": round(success_rate, 3)
        }
