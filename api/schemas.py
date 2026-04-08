from pydantic import BaseModel


class PredictionRequest(BaseModel):
    year: int
    month: int
    quarter: int
    month_sin: float
    month_cos: float
    lag_1: float
    lag_3: float
    lag_6: float
    lag_12: float
    rolling_mean_3: float
    rolling_mean_6: float
    rolling_std_3: float
    total_over_4hrs: float
    total_emergency_admissions: float
    total_booked_attendances: float
    total_dta_waits: float


class PredictionResponse(BaseModel):
    predicted_attendance: float
