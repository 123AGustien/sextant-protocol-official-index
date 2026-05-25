import json
import os
from orbital_engine import OrbitalEngine

# -----------------------------------------
# Initialize engine
# -----------------------------------------
engine = OrbitalEngine()

# -----------------------------------------
# Build dependency graph
# -----------------------------------------
engine.add_node("A", criticality=5)
engine.add_node("B", criticality=4)
engine.add_node("C", criticality=3)

engine.add_edge("A", "B")
engine.add_edge("B", "C")

# -----------------------------------------
# Inject failure
# -----------------------------------------
engine.fail_node("A")

# -----------------------------------------
# Run simulation
# -----------------------------------------
print("=== ORBITAL SIMULATION START ===")

history = []
propagated_impacts = set()

for i in range(3):
    state = engine.step()

    print(f"Step {state['time']}: {state['states']}")

    history.append({
        "step": state["time"],
        "states": state["states"]
    })

    # -----------------------------------------
    # DETECT IMPACTED NODES (REAL DERIVATION)
    # -----------------------------------------
    for node, status in state["states"].items():
        if status != "HEALTHY":
            propagated_impacts.add(node)

print("=== SIMULATION END ===")

# -----------------------------------------
# OUTPUT DIRECTORY (CI LAYER)
# -----------------------------------------
os.makedirs("output", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# -----------------------------------------
# SEXTANT CASCADE OUTPUT (DETERMINISTIC)
# -----------------------------------------
cascade_output = {
    "domain": "orbital",
    "failed_nodes": [n for n, s in state["states"].items() if s == "FAILED"],
    "impacts_on_orbital": list(propagated_impacts),
    "history": history
}

with open("output/cascade_execution.json", "w") as f:
    json.dump(cascade_output, f, indent=2)

with open("logs/run.log", "w") as f:
    f.write("Orbital simulation completed successfully\n")

print("✔ Cascade output written to output/cascade_execution.json")
