from fastapi import FastAPI
from api.schemas import PredictionRequest, PredictionResponse
from api.utils import load_model, prepare_input

app = FastAPI(title="NHS A&E Forecast API")

model = load_model()


@app.get("/")
def root():
    return {"message": "NHS A&E Forecast API is running"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    input_df = prepare_input(request.model_dump())
    prediction = model.predict(input_df)[0]
    return PredictionResponse(predicted_attendance=float(prediction))
