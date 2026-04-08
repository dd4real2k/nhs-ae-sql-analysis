from pathlib import Path
import joblib
import pandas as pd

from src.config import MODELS_DIR, DEFAULT_MODEL_FILENAME, MODEL_FEATURES


MODEL_PATH = MODELS_DIR / DEFAULT_MODEL_FILENAME



def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)


def prepare_input(data: dict) -> pd.DataFrame:
    df = pd.DataFrame([data])
    missing = [col for col in MODEL_FEATURES if col not in df.columns]
    if missing:
        raise ValueError(f"Missing input features: {missing}")
    return df[MODEL_FEATURES]

def model_metadata() -> dict:
    return {
        "model_path": str(MODEL_PATH),
        "model_filename": DEFAULT_MODEL_FILENAME,
        "features_count": len(MODEL_FEATURES),
        "features": MODEL_FEATURES,
    }
