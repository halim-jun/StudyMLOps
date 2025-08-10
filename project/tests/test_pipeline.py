import os
import pandas as pd
import numpy as np
from pathlib import Path
from project.src.pipeline import ModelPipeline




def test_process_and_split():    
    tmp_path = "project/tests/test_data.csv"
    mp = ModelPipeline(tmp_path)
    processed = mp.preprocess_data()
    assert {"Stage_fear_bool","Drained_after_socializing_bool","extrovert"}.issubset(processed.columns)
    train_data, test_data = mp.train_test_split(processed, tmp_path)
    assert not train_data.empty
    assert not test_data.empty
    mp.train_model(train_data)
    assert mp.logistic_clf is not None
    assert mp.predict(test_data) is not None
    assert (tmp_path / "train_data.csv").exists()
    assert (tmp_path / "test_data.csv").exists()
    assert (tmp_path / "logistic_clf.joblib").exists()
    model = mp.train_model(train_data)
    mp.save_model(tmp_path / "logistic_clf.joblib")
    prediction = mp.predict(test_data)
    assert model is not None
    assert prediction is not None
    assert len(prediction) == len(test_data)
    assert len(prediction) == len(test_data)
    prediction_set = np.unique(prediction)
    uniq = set(map(int, np.unique(prediction_set)))
    assert uniq.issubset({0,1})