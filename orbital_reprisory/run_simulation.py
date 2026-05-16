from orbital_reprisory.core.orbital_engine import OrbitalEngine
from orbital_reprisory.core.scenario_loader import ScenarioLoader
import json


# -------------------------------------------------
# MAIN SIMULATION RUNNER
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
        for node in scenario["nodes"]:
            if isinstance(node, dict):
                self.engine.add_node(node["id"], node.get("criticality", 5))
            else:
                self.engine.add_node(node)

        # build edges
        for dep in scenario["dependencies"]:
            self.engine.add_edge(dep["from"], dep["to"])

        # initial failure
        if scenario.get("initial_failure"):
            self.engine.fail_node(scenario["initial_failure"])

        return scenario

    # -------------------------------------------------
    # EXECUTE SIMULATION
    # -------------------------------------------------
    def run(self, steps=5):
        print("\n🧭 Orbital Reprisory Simulation Starting...\n")

        for i in range(steps):
            result = self.engine.step()

            print(f"Step {result['time']}")
            print("States:", result["states"])

            if "interventions" in result:
                print("Interventions:", result["interventions"])

            print("-" * 40)

        print("\n✅ Simulation Complete\n")


# -------------------------------------------------
# ENTRY POINT
# -------------------------------------------------
if __name__ == "__main__":
    runner = SimulationRunner("scenario.json")
    runner.setup()
    runner.run(steps=10)
