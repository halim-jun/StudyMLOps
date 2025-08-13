from pathlib import Path
from typing import Set

import numpy as np
import pandas as pd

from project.src.pipeline import ModelPipeline


def _make_tiny_raw_csv(tmp_dir: Path) -> Path:
    df = pd.DataFrame(
        {
            "Personality": [
                "Extrovert",
                "Introvert",
                "Extrovert",
                "Introvert",
                "Extrovert",
                "Introvert",
            ],
            "Stage_fear": ["Yes", "No", "Yes", "No", "No", "Yes"],
            "Drained_after_socializing": ["Yes", "No", "No", "Yes", "No", "Yes"],
        }
    )
    csv_path = tmp_dir / "tiny.csv"
    df.to_csv(csv_path, index=False)
    return csv_path


def test_process_train_predict(tmp_path: Path) -> None:
    raw_csv = _make_tiny_raw_csv(Path(tmp_path))
    mp = ModelPipeline(str(raw_csv))
    processed = mp.preprocess_data()
    assert {"Stage_fear_bool", "Drained_after_socializing_bool", "extrovert"}.issubset(
        processed.columns
    )

    train_df, test_df = mp.train_test_split(processed, str(tmp_path))
    assert not train_df.empty and not test_df.empty

    mp.train_model(train_df)
    preds = mp.predict(test_df)
    assert len(preds) == len(test_df)
    uniq: Set[int] = set(map(int, np.unique(preds)))
    assert uniq.issubset({0, 1})

    # ensure artifacts are written
    assert (Path(tmp_path) / "train_data.csv").exists()
    assert (Path(tmp_path) / "test_data.csv").exists()
    mp.save_model(str(Path(tmp_path) / "logistic_clf.joblib"))
    assert (Path(tmp_path) / "logistic_clf.joblib").exists()
