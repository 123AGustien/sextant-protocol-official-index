"""
🧾 Governance Gate Engine v1
Sextant Protocol Enforcement Layer

Blocks or allows system execution based on severity.
"""

class GovernanceGateEngineV1:

    def evaluate(self, severity_level: str) -> bool:

        if severity_level == "LOW":
            return True

        if severity_level == "MEDIUM":
            return True

        if severity_level == "HIGH":
            return False

        if severity_level == "CRITICAL":
            return False

        return False
