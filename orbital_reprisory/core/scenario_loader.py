import json


class ScenarioLoader:
    """
    Orbital Reprisory Scenario Loader

    Purpose:
    - Standardise simulation inputs
    - Load JSON-based scenarios
    - Validate node + dependency structure
    """

    def __init__(self, path=None):
        self.path = path

    # -------------------------------------------------
    # LOAD FROM FILE
    # -------------------------------------------------
    def load_from_file(self, path=None):
        path = path or self.path

        if not path:
            raise ValueError("No scenario file path provided")

        with open(path, "r") as f:
            data = json.load(f)

        return self.validate(data)

    # -------------------------------------------------
    # VALIDATION LAYER
    # -------------------------------------------------
    def validate(self, scenario: dict) -> dict:
        required_keys = ["scenario_name", "nodes", "dependencies"]

        for key in required_keys:
            if key not in scenario:
                raise ValueError(f"Missing required field: {key}")

        # normalize optional field
        if "initial_failure" not in scenario:
            scenario["initial_failure"] = None

        return scenario

    # -------------------------------------------------
    # BUILD READY SCENARIO
    # -------------------------------------------------
    def build(self, scenario: dict) -> dict:
        """
        Converts raw input into engine-ready format
        """
        return self.validate(scenario)
