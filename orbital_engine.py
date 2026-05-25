import random


class Node:
    def __init__(self, node_id, criticality=5):
        self.id = node_id
        self.criticality = criticality
        self.state = "healthy"

        self.resilience = 1.0
        self.exposure = 0.0

        self.is_isolated = False
        self.protected = False


class Edge:
    def __init__(self, from_id, to_id, weight=0.5):
        self.from_id = from_id
        self.to_id = to_id
        self.weight = weight


class OrbitalEngine:

    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.time = 0

        self.resilience_history = []
        self.interventions = []

    def add_node(self, node_id, criticality=5):
        self.nodes[node_id] = Node(node_id, criticality)

    def add_edge(self, from_id, to_id, weight=0.5):
        self.edges.append(Edge(from_id, to_id, weight))

    def fail_node(self, node_id):
        if node_id in self.nodes:
            self.nodes[node_id].state = "failed"

    def calculate_exposure(self, node):
        exposure = 0.0

        for edge in self.edges:
            if edge.to_id == node.id:
                from_node = self.nodes.get(edge.from_id)
                if from_node and from_node.state == "failed":
                    exposure += edge.weight

        node.exposure = min(1.0, exposure)

    def compute_resilience(self, node):
        pressure = node.exposure * (node.criticality / 10)
        return max(0.0, node.resilience - pressure)

    def propagate(self):
        newly_failed = set()

        for node in self.nodes.values():
            if node.state != "healthy":
                continue

            resilience = self.compute_resilience(node)
            risk = node.exposure * node.criticality
            probability = min(1.0, risk / (resilience + 0.1))

            if random.random() < probability:
                newly_failed.add(node.id)

        for nid in newly_failed:
            self.nodes[nid].state = "failed"

        return newly_failed

    def control_layer(self):
        risky_nodes = []

        for node in self.nodes.values():
            risk = node.exposure * node.criticality
            if risk > 0.6 and node.state == "healthy":
                risky_nodes.append(node)

        for node in risky_nodes:
            self.isolate_node(node)
            self.protect_node(node)

        self.reroute_edges()

    def isolate_node(self, node):
        node.is_isolated = True
        node.exposure *= 0.3

        self.interventions.append({
            "time": self.time,
            "action": "isolate",
            "node": node.id
        })

    def protect_node(self, node):
        node.protected = True
        node.resilience = min(1.0, node.resilience + 0.25)

        self.interventions.append({
            "time": self.time,
            "action": "protect",
            "node": node.id
        })

    def reroute_edges(self):
        for edge in self.edges:
            from_node = self.nodes.get(edge.from_id)
            if from_node and from_node.is_isolated:
                edge.weight *= 0.5

    def system_resilience_index(self):
        total = len(self.nodes)
        if total == 0:
            return 0.0

        healthy = sum(1 for n in self.nodes.values() if n.state == "healthy")
        return healthy / total

    def step(self):
        self.time += 1

        for node in self.nodes.values():
            self.calculate_exposure(node)

        newly_failed = self.propagate()
        self.control_layer()

        ri = self.system_resilience_index()
        self.resilience_history.append(ri)

        return {
            "time": self.time,
            "newly_failed": list(newly_failed),
            "system_resilience_index": ri,
            "interventions": self.interventions[-5:],
            "states": {n.id: n.state for n in self.nodes.values()}
        }
