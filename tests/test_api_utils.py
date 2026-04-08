import pytest
from api.utils import prepare_input
from src.config import MODEL_FEATURES


def valid_payload():
    return {
        "year": 2026,
        "month": 2,
        "quarter": 1,
        "month_sin": 0.5,
        "month_cos": 0.8,
        "lag_1": 100.0,
        "lag_3": 100.0,
        "lag_6": 100.0,
        "lag_12": 100.0,
        "rolling_mean_3": 100.0,
        "rolling_mean_6": 100.0,
        "rolling_std_3": 10.0,
        "total_over_4hrs": 50.0,
        "total_emergency_admissions": 40.0,
        "total_booked_attendances": 20.0,
        "total_dta_waits": 5.0,
    }

def test_prepare_input_returns_expected_shape():
    df = prepare_input(valid_payload())
    assert df.shape == (1, len(MODEL_FEATURES))

def test_prepare_input_returns_expected_columns_in_order():
    df = prepare_input(valid_payload())
    assert list(df.columns) == MODEL_FEATURES

def test_prepare_input_raises_for_missing_feature():
    payload = valid_payload()
    payload.pop("lag_1")

    with pytest.raises(ValueError, match="Missing input features"):
        prepare_input(payload)
