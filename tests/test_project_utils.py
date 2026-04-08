import pandas as pd
from src.project_utils import clean_column_name, clean_columns, create_time_features


def test_clean_column_name():
    assert clean_column_name("A&E Attendances Type 1") == "aande_attendances_type_1"


def test_clean_columns():
    df = pd.DataFrame(columns=["A&E Attendances Type 1", "Other Emergency Admissions"])
    cleaned = clean_columns(df)
    assert "aande_attendances_type_1" in cleaned.columns
    assert "other_emergency_admissions" in cleaned.columns

def test_create_time_features():
    df = pd.DataFrame({"period": ["2026-02-01"]})
    out = create_time_features(df)

    assert "year" in out.columns
    assert "month" in out.columns
    assert "quarter" in out.columns
    assert "month_sin" in out.columns
    assert "month_cos" in out.columns
    assert out.loc[0, "year"] == 2026
    assert out.loc[0, "month"] == 2
    assert out.loc[0, "quarter"] == 1
