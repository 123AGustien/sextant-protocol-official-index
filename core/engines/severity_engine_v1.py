"""
📊 Severity Engine v1
Sextant Protocol Engine Layer

Converts cascade outputs into risk scores.
"""

class SeverityEngineV1:

    def compute_risk(self, DS, PS, CD, OD):

        if OD == 0:
            return float("inf")

        return (DS * PS * CD) / OD

    def classify(self, risk_score):

        if risk_score < 0.3:
            return "LOW"

        elif risk_score < 0.7:
            return "MEDIUM"

        elif risk_score < 1.5:
            return "HIGH"

        else:
            return "CRITICAL"
