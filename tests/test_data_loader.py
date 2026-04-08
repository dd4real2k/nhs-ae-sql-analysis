from pathlib import Path
import pandas as pd
import pytest

from src.data_loader import list_csv_files, read_csv_file, validate_required_columns


def test_list_csv_files(tmp_path: Path):
    file1 = tmp_path / "a.csv"
    file1.write_text("x\n1\n")
    files = list_csv_files(str(tmp_path))
    assert len(files) == 1
    assert files[0].name == "a.csv"

def test_read_csv_file_adds_source_file(tmp_path: Path):
    file1 = tmp_path / "sample.csv"
    file1.write_text("col1,col2\n1,2\n")

    df = read_csv_file(file1)
    assert "source_file" in df.columns
    assert df.loc[0, "source_file"] == "sample.csv"


def test_validate_required_columns_passes():
    df = pd.DataFrame({"a": [1], "b": [2]})
    validate_required_columns(df, ["a", "b"])


def test_validate_required_columns_raises():
    df = pd.DataFrame({"a": [1]})

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_required_columns(df, ["a", "b"])
