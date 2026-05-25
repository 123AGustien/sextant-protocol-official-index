"""
🧾 Governance Decision Engine v1
Sextant Protocol Engine Layer

Transforms severity into system decisions.
"""

class GovernanceDecisionEngineV1:

    def decide(self, severity_level):

        if severity_level == "LOW":
            return "APPROVE"

        elif severity_level == "MEDIUM":
            return "MONITOR"

        elif severity_level == "HIGH":
            return "RESTRICT"

        elif severity_level == "CRITICAL":
            return "BLOCK"

        return "UNKNOWN"
