import networkx as nx

class GraphEngine:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id, failure_prob=0.1):
        self.graph.add_node(node_id, failure_prob=failure_prob)

    def add_edge(self, from_node, to_node):
        self.graph.add_edge(from_node, to_node)

    def get_downstream(self, node_id):
        return list(self.graph.successors(node_id))

    def get_failure_prob(self, node_id):
        return self.graph.nodes[node_id]["failure_prob"]

    def nodes(self):
        return list(self.graph.nodes)
