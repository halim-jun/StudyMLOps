import sys
from pathlib import Path
from typing import Dict, Any

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Ensure repo root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

app = FastAPI(title="Personality Prediction API", version="1.0.0")

# Pydantic model for request validation
#Pydantic의 BaseModel: 데이터 검증과 직렬화를 자동으로 해주는 클래스
#들어오는 JSON 데이터를 파이썬 객체로 변환하면서 타입 체크, 필수 필드 검증 등을 자동 처리
class PredictionRequest(BaseModel):
    Stage_fear_bool: bool
    Drained_after_socializing_bool: bool
    Time_spent_Alone: float
    Social_event_attendance: float
    Going_outside: float
    Friends_circle_size: float
    Post_frequency: float

# Global model variable
model = None

@app.on_event("startup")
async def load_model():
    """Load the trained model on startup"""
    global model
    try:
        model_path = Path(__file__).parent / "logistic_clf.joblib"
        if model_path.exists():
            model = joblib.load(model_path)
            print(f"Model loaded successfully from {model_path}")
        else:
            print(f"Warning: Model file not found at {model_path}")
    except Exception as e:
        print(f"Error loading model: {e}")

@app.get("/")
def root():
    return {
        "message": "Personality Prediction API", 
        "status": "running",
        "model_loaded": model is not None
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

@app.post("/predict")
def predict(request: PredictionRequest) -> Dict[str, Any]:
    """
    Predict personality type based on input features
    
    Example request:
    {
        "Stage_fear_bool": true,
        "Drained_after_socializing_bool": false
        "Time_spent_Alone": 10.0,
        "Social_event_attendance": 10.0,
        "Going_outside": 10.0,
        "Friends_circle_size": 10.0,
        "Post_frequency": 10.0,
    }
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Convert request to DataFrame (same format as training)
        input_data = pd.DataFrame([{
            "Time_spent_Alone": request.Time_spent_Alone,
            "Social_event_attendance": request.Social_event_attendance,
            "Going_outside": request.Going_outside,
            "Friends_circle_size": request.Friends_circle_size,
            "Post_frequency": request.Post_frequency,
            "Stage_fear_bool": request.Stage_fear_bool,
            "Drained_after_socializing_bool": request.Drained_after_socializing_bool
        }])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0]
        
        # Convert to human-readable result
        personality_type = "Extrovert" if prediction else "Introvert"
        confidence = float(max(prediction_proba))
        
        return {
            "prediction": personality_type,
            "confidence": round(confidence, 3),
            "probabilities": {
                "Introvert": round(float(prediction_proba[0]), 3),
                "Extrovert": round(float(prediction_proba[1]), 3)
            },
            "input_features": {
                "Stage_fear": request.Stage_fear_bool,
                "Drained_after_socializing": request.Drained_after_socializing_bool,
                "Time_spent_Alone": request.Time_spent_Alone,
                "Social_event_attendance": request.Social_event_attendance,
                "Going_outside": request.Going_outside,
                "Friends_circle_size": request.Friends_circle_size,
                "Post_frequency": request.Post_frequency,
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")