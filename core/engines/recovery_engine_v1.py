"""
🔁 Recovery Engine v1
Sextant Protocol Engine Layer

Applies system recovery actions after cascade.
"""

class RecoveryEngineV1:

    def recover(self, node_states, decision):

        updated = node_states.copy()

        if decision == "APPROVE":
            return updated

        if decision == "MONITOR":
            for n in updated:
                if updated[n] == "FAILED":
                    updated[n] = "DEGRADED"

        if decision == "RESTRICT":
            for n in updated:
                if updated[n] == "HEALTHY":
                    updated[n] = "DEGRADED"

        if decision == "BLOCK":
            for n in updated:
                updated[n] = "ISOLATED"

        return updated
