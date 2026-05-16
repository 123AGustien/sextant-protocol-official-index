 Orbital Reprisory Reprisory - Core Engine

class Node:
    def __init__(self, node_id, criticality=5):
        self.id = node_id
        self.criticality = criticality
        self.state = "healthy"


class Edge:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node


class OrbitalEngine:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.time = 0

    def add_node(self, node_id, criticality=5):
        self.nodes[node_id] = Node(node_id, criticality)

    def add_edge(self, from_id, to_id):
        self.edges.append(Edge(from_id, to_id))

    def fail_node(self, node_id):
        if node_id in self.nodes:
            self.nodes[node_id].state = "failed"

    def step(self):
        self.time += 1

        # Simple propagation rule (v1)
        for edge in self.edges:
            from_node = self.nodes.get(edge.from_node)
            to_node = self.nodes.get(edge.to_node)

            if from_node and to_node:
                if from_node.state == "failed":
                    to_node.state = "degraded"

        return {
            "time": self.time,
            "states": {n: self.nodes[n].state for n in self.nodes}
        }
