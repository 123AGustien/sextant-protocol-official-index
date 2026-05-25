"""
📊 Cascade Graph Engine v1
Sextant Protocol Visualization Layer

Generates simple SVG graph representation of cascade flow.
"""

class CascadeGraphEngineV1:

    def generate_svg(self, cascade_data: dict) -> str:

        source = cascade_data.get("source_domain", "unknown")
        target = cascade_data.get("target_domain", "unknown")
        trigger = cascade_data.get("trigger", "event")

        svg = f"""
        <svg width="600" height="200" xmlns="http://www.w3.org/2000/svg">

            <rect x="50" y="70" width="150" height="50" fill="lightblue"/>
            <text x="75" y="100">{source}</text>

            <line x1="200" y1="95" x2="350" y2="95"
                  stroke="black" stroke-width="2"/>

            <rect x="350" y="70" width="200" height="50" fill="lightcoral"/>
            <text x="370" y="100">{target}</text>

            <text x="220" y="60">{trigger}</text>

        </svg>
        """

        return svg
