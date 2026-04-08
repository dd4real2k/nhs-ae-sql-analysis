from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from api.schemas import PredictionRequest, PredictionResponse
from api.utils import load_model, prepare_input, model_metadata

MODEL = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global MODEL
    MODEL = load_model()
    yield

app = FastAPI(
    title="NHS A&E Forecast API",
    description="API for predicting monthly NHS A&E attendances from engineered operational features.",
    version="1.0.0",
    lifespan=lifespan,
)

@app.get("/")
def root():
    return {
        "message": "NHS A&E Forecast API is running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metadata")
def metadata():
    return model_metadata()


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    global MODEL

    if MODEL is None:
        raise HTTPException(status_code=503, detail="Model is not loaded yet.")

    try:
        input_df = prepare_input(request.model_dump())
        prediction = MODEL.predict(input_df)[0]
        return PredictionResponse(predicted_attendance=float(prediction))
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {exc}") from exc
