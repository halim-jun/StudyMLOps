import runpy
from pathlib import Path


def test_training_entrypoint_runs(monkeypatch, tmp_path):
    # Run the training module as a script under pytest so coverage captures it
    # Save artifacts into a temp directory to avoid polluting the repo
    monkeypatch.chdir(Path(tmp_path))
    runpy.run_module("project.src.training", run_name="__main__")
    # Model artifact should be created in the tmp directory
    assert (Path(tmp_path) / "logistic_clf.joblib").exists()
