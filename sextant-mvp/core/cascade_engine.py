import random

class CascadeEngine:
    def __init__(self, graph_engine):
        self.graph = graph_engine.graph

    def run(self, initial_failures):
        """
        Simulates failure propagation through dependency graph.
        """

        failed = set(initial_failures)
        queue = list(initial_failures)

        while queue:
            current = queue.pop(0)

            # get downstream nodes
            downstream = list(self.graph.successors(current))

            for node in downstream:
                if node in failed:
                    continue

                base_prob = self.graph.nodes[node]["failure_prob"]

                # cascade amplification (key concept)
                cascade_factor = 0.5

                adjusted_prob = min(1.0, base_prob + cascade_factor)

                if random.random() < adjusted_prob:
                    failed.add(node)
                    queue.append(node)

        return {
            "failed_nodes": list(failed),
            "cascade_depth": len(failed)
        }
