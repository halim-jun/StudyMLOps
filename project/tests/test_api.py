import pytest
from fastapi.testclient import TestClient
from pathlib import Path
import sys
import joblib

# Ensure repo root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from project.src.main import app

# Load the actual model for testing
@pytest.fixture(scope="module", autouse=True)
def load_model_for_tests():
    """Load the actual trained model for API tests"""
    from project.src import main
    
    # Load the actual model file
    model_path = Path(__file__).parent.parent / "src" / "logistic_clf.joblib"
    if model_path.exists():
        main.model = joblib.load(model_path)
        print(f"Loaded model from {model_path}")
    else:
        raise FileNotFoundError(f"Model file not found at {model_path}")


#app = FastAPI()가 들어있는 모듈을 import
client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "running"


def test_health_endpoint():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"


def test_predict_valid_input():
    """Test prediction with valid input"""
    response = client.post(
        "/predict",
        json={
            "Time_spent_Alone": 0,
            "Social_event_attendance": 0,
            "Going_outside": 0,
            "Friends_circle_size": 0,
            "Post_frequency": 0,
            "Stage_fear_bool": True,
            "Drained_after_socializing_bool": False,
        }
    )
    assert response.status_code == 200
    data = response.json()
    
    # Check response structure
    assert "prediction" in data
    assert "confidence" in data
    assert "probabilities" in data
    assert "input_features" in data
    
    # Check prediction value
    assert data["prediction"] in ["Extrovert", "Introvert"]
    
    # Check confidence is between 0 and 1
    assert 0 <= data["confidence"] <= 1
    
    # Check probabilities sum to 1 (approximately)
    probs = data["probabilities"]
    assert abs(probs["Introvert"] + probs["Extrovert"] - 1.0) < 0.001


def test_predict_invalid_input_missing_field():
    """Test prediction with missing required field"""
    response = client.post(
        "/predict",
        json={
            "Social_event_attendance": 0,
            "Going_outside": 0,
            "Friends_circle_size": 0,
            "Post_frequency": 0,
            "Stage_fear_bool": True,
            "Drained_after_socializing_bool": False,
        }
    )
    assert response.status_code == 422  # Validation error


def test_predict_invalid_input_wrong_type():
    """Test prediction with wrong data type"""
    response = client.post(
        "/predict",
        json={
            "Time_spent_Alone": "invalid_string",  # Should be float
            "Social_event_attendance": 0,
            "Going_outside": 0,
            "Friends_circle_size": 0,
            "Post_frequency": 0,
            "Stage_fear_bool": True,
            "Drained_after_socializing_bool": False
        }
    )
    assert response.status_code == 422  # Validation error




@pytest.mark.parametrize("stage_fear,drained", [
    (True, True),
    (True, False),
    (False, True),
    (False, False),
])
def test_predict_all_combinations(stage_fear, drained):
    """Test all possible input combinations"""
    response = client.post(
        "/predict",
        json={
            "Time_spent_Alone": 0,
            "Social_event_attendance": 0,
            "Going_outside": 0,
            "Friends_circle_size": 0,
            "Post_frequency": 0,
            "Stage_fear_bool": stage_fear,
            "Drained_after_socializing_bool": drained,
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] in ["Extrovert", "Introvert"]
