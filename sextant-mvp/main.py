from sextant_mvp.experiments.runner import ExperimentRunner

if __name__ == "__main__":
    runner = ExperimentRunner()

    scenarios = [
        "sextant-mvp/scenarios/small.json",
        "sextant-mvp/scenarios/medium.json",
        "sextant-mvp/scenarios/stress.json"
    ]

    results = runner.run_all(scenarios)

    print("\nEXPERIMENT RESULTS:\n")
    for r in results:
        print(r)
        print("\n----------------------\n")
