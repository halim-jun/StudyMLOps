from pathlib import Path
import sys

# Ensure repo root is on sys.path so absolute package import always works
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from project.src.pipeline import ModelPipeline
from sklearn.metrics import classification_report

if __name__ == "__main__":
    # Get the project root directory (two levels up from this script)
    project_root = Path(__file__).parent.parent.parent
    data_path = project_root / "project" / "data"

    model_pipeline = ModelPipeline(str(data_path / "personality_dataset.csv"))
    data = model_pipeline.load_data()
    data = model_pipeline.preprocess_data()
    train_data, test_data = model_pipeline.train_test_split(data, str(data_path))
    model_pipeline.train_model(train_data)
    predictions = model_pipeline.predict(test_data)
    report = classification_report(test_data["extrovert"], predictions)
    model_pipeline.save_model("logistic_clf.joblib")
    print(report)
