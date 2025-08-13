import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class ModelPipeline:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.train_data = None
        self.test_data = None
        self.logistic_clf = None
        self.random_forest_clf = None
        self.svm_clf = None
        self.knn_clf = None
        self.decision_tree_clf = None
        self.naive_bayes_clf = None
        self.gradient_boosting_clf = None
        self.xgboost_clf = None

    def load_data(self):
        return pd.read_csv(self.data_path)

    def preprocess_data(self):
        data = self.load_data()
        self.data = data

        data = data.dropna()
        data = data.drop_duplicates()
        data_processed = data.copy()

        data_processed.loc[data_processed["Personality"] == "Extrovert", "extrovert"] = 1
        data_processed.loc[data_processed["Personality"] == "Introvert", "extrovert"] = 0
        data_processed.loc[data_processed["Stage_fear"] == "Yes", "Stage_fear_bool"] = 1
        data_processed.loc[data_processed["Stage_fear"] == "No", "Stage_fear_bool"] = 0
        data_processed.loc[
            data_processed["Drained_after_socializing"] == "Yes",
            "Drained_after_socializing_bool",
        ] = 1
        data_processed.loc[
            data_processed["Drained_after_socializing"] == "No",
            "Drained_after_socializing_bool",
        ] = 0
        data_processed.drop(
            columns=["Personality", "Stage_fear", "Drained_after_socializing"],
            inplace=True,
        )
        data_processed[
            ["Stage_fear_bool", "Drained_after_socializing_bool", "extrovert"]
        ] = data_processed[
            ["Stage_fear_bool", "Drained_after_socializing_bool", "extrovert"]
        ].astype(
            bool
        )
        self.data_processed = data_processed
        return data_processed

    def train_test_split(self, data: pd.DataFrame, path: str, test_size: float = 0.2):
        train_data, test_data = train_test_split(data, test_size=test_size, random_state=42)
        train_data.to_csv(path + "/train_data.csv", index=False)
        test_data.to_csv(path + "/test_data.csv", index=False)
        self.train_data = train_data
        self.test_data = test_data
        return train_data, test_data

    def train_model(self, data: pd.DataFrame):
        model = LogisticRegression()
        model.fit(data.drop(columns=["extrovert"]), data["extrovert"])
        self.logistic_clf = model
        joblib.dump(model, "logistic_clf.joblib")
        return model

    def predict(self, data: pd.DataFrame):
        return self.logistic_clf.predict(data.drop(columns=["extrovert"]))

    def save_model(self, path: str):
        joblib.dump(self.logistic_clf, path)
