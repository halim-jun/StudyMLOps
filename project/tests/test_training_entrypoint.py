import runpy
from pathlib import Path
from _pytest.monkeypatch import MonkeyPatch


def test_training_entrypoint_runs(monkeypatch: MonkeyPatch, tmp_path: Path) -> None:
    # Run the training module as a script under pytest so coverage captures it
    # Save artifacts into a temp directory to avoid polluting the repo
    monkeypatch.chdir(Path(tmp_path))
    # Run as a module to respect package-relative imports
    runpy.run_module("project.src.training", run_name="__main__")
    # Model artifact should be created in the tmp directory
    assert (Path(tmp_path) / "logistic_clf.joblib").exists()
