from orbital_engine import OrbitalEngine

# Initialize engine
engine = OrbitalEngine()

# Build small dependency graph
engine.add_node("A", criticality=5)
engine.add_node("B", criticality=4)
engine.add_node("C", criticality=3)

engine.add_edge("A", "B")
engine.add_edge("B", "C")

# Inject failure
engine.fail_node("A")

# Run simulation steps
print("=== ORBITAL SIMULATION START ===")

for i in range(3):
    state = engine.step()
    print(f"Step {state['time']}: {state['states']}")

print("=== SIMULATION END ===")
