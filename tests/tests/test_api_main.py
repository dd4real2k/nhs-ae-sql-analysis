from fastapi.testclient import TestClient
import api.main as main_module

from api.main import app


class DummyModel:
    def predict(self, df):
        return [12345.67]


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


def test_root_endpoint():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_endpoint():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict_endpoint(monkeypatch):
    monkeypatch.setattr(main_module, "MODEL", DummyModel())
    client = TestClient(app)

    response = client.post("/predict", json=valid_payload())
    assert response.status_code == 200
    assert response.json()["predicted_attendance"] == 12345.67
