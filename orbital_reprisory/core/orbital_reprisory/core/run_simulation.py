from orbital_reprisory.core.orbital_engine import OrbitalEngine

# Initialize engine
engine = OrbitalEngine()

# Build dependency graph
engine.add_node("A", criticality=5)
engine.add_node("B", criticality=4)
engine.add_node("C", criticality=3)

engine.add_edge("A", "B")
engine.add_edge("B", "C")

# Inject failure
engine.fail_node("A")

print("=== ORBITAL SIMULATION START ===")

# Run simulation steps
for i in range(3):
    result = engine.step()
    print(f"Step {result['time']}: {result['states']}")

print("=== SIMULATION END ===")
