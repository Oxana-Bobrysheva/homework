from typing import Any
from unittest.mock import patch

import pandas as pd
import pytest

from src.reading_excel import reading_xlsx


@pytest.fixture
def mock_read_excel():
    with patch("pandas.read_excel") as mock:
        yield mock


def test_reading_xlsx_success(mock_read_excel):
    # Arrange
    file_name = "test.xlsx"
    data = {"Column1": [1, 2, 3], "Column2": [4, 5, 6]}
    df = pd.DataFrame(data)
    mock_read_excel.return_value = df

    # Act
    result = reading_xlsx(file_name)

    # Assert
    assert len(result) == 3
    assert result[0] == {"Column1": 1, "Column2": 4}
    assert result[1] == {"Column1": 2, "Column2": 5}
    assert result[2] == {"Column1": 3, "Column2": 6}


def test_reading_xlsx_file_not_found() -> None:
    # Act and Assert
    result = reading_xlsx("non_existent_file.xlsx")
    assert result == []


def test_reading_xlsx_error_occurred(mock_read_excel: Any) -> None:
    # Arrange
    file_name = "test.xlsx"
    mock_read_excel.side_effect = Exception("Error occurred")

    # Act and Assert
    result = reading_xlsx(file_name)
    assert result == []
