from orbital_reprisory.core.orbital_engine import OrbitalEngine
from orbital_reprisory.core.scenario_loader import ScenarioLoader
import os


# -------------------------------------------------
# SIMULATION RUNNER (POLISHED v1)
# -------------------------------------------------
class SimulationRunner:

    def __init__(self, scenario_path):
        self.loader = ScenarioLoader()
        self.engine = OrbitalEngine()
        self.scenario_path = scenario_path

    # -------------------------------------------------
    # LOAD SCENARIO INTO ENGINE
    # -------------------------------------------------
    def setup(self):
        scenario = self.loader.load_from_file(self.scenario_path)

        # build nodes
        for node in scenario.get("nodes", []):
            if isinstance(node, dict):
                self.engine.add_node(
                    node["id"],
                    node.get("criticality", 5)
                )
            else:
                self.engine.add_node(node)

        # build edges
        for dep in scenario.get("dependencies", []):
            self.engine.add_edge(dep["from"], dep["to"])

        # initial failure
        initial_failure = scenario.get("initial_failure")
        if initial_failure:
            self.engine.fail_node(initial_failure)

        return scenario

    # -------------------------------------------------
    # EXECUTE SIMULATION
    # -------------------------------------------------
    def run(self, steps=5):
        print("\n🧭 Orbital Reprisory Simulation Starting...\n")

        for _ in range(steps):
            result = self.engine.step()

            print(f"Step {result['time']}")
            print("States:", result["states"])

            if result.get("interventions"):
                print("Interventions:", result["interventions"])

            print("-" * 40)

        print("\n✅ Simulation Complete\n")


# -------------------------------------------------
# ENTRY POINT (CI SAFE)
# -------------------------------------------------
if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    scenario_path = os.path.join(base_path, "scenario.json")

    runner = SimulationRunner(scenario_path)
    runner.setup()
    runner.run(steps=10)
