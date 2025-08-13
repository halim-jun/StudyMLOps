from pathlib import Path
from sklearn.metrics import classification_report
from pipeline import ModelPipeline

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
    classification_report = classification_report(test_data["extrovert"], predictions)
    model_pipeline.save_model("logistic_clf.joblib")
    print(classification_report)
