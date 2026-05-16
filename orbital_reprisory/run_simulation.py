from orbital_reprisory.core.orbital_engine import OrbitalEngine
from orbital_reprisory.core.scenario_loader import ScenarioLoader
import os


# -------------------------------------------------
# SIMULATION RUNNER (v2 STABLE)
# -------------------------------------------------
class SimulationRunner:

    def __init__(self, scenario_path: str):
        self.loader = ScenarioLoader()
        self.engine = OrbitalEngine()
        self.scenario_path = scenario_path

    # -------------------------------------------------
    # LOAD SCENARIO INTO ENGINE
    # -------------------------------------------------
    def setup(self) -> dict:
        scenario = self.loader.load_from_file(self.scenario_path)

        # Defensive validation (CI SAFE)
        if not isinstance(scenario, dict):
            raise ValueError("Scenario must be a dictionary")

        # build nodes
        for node in scenario.get("nodes", []):
            if isinstance(node, dict):
                self.engine.add_node(
                    node.get("id"),
                    node.get("criticality", 5)
                )
            else:
                self.engine.add_node(node)

        # build edges
        for dep in scenario.get("dependencies", []):
            self.engine.add_edge(dep.get("from"), dep.get("to"))

        # initial failure
        initial_failure = scenario.get("initial_failure")
        if initial_failure:
            self.engine.fail_node(initial_failure)

        return scenario

    # -------------------------------------------------
    # EXECUTE SIMULATION
    # -------------------------------------------------
    def run(self, steps: int = 5) -> dict:
        print("\n🧭 Orbital Reprisory Simulation Starting...\n")

        final_state = {}

        for _ in range(steps):
            result = self.engine.step()

            final_state = result  # keep last snapshot

            print(f"Step {result.get('time')}")
            print("States:", result.get("states", {}))

            if result.get("interventions"):
                print("Interventions:", result["interventions"])

            print("-" * 40)

        print("\n✅ Simulation Complete\n")

        return final_state


# -------------------------------------------------
# ENTRY POINT (CI SAFE + PATH RESOLVED)
# -------------------------------------------------
if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    scenario_path = os.path.join(base_path, "scenario.json")

    runner = SimulationRunner(scenario_path)
    runner.setup()
    runner.run(steps=10)
