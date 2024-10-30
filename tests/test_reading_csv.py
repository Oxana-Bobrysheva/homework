import pytest
from unittest.mock import mock_open, patch
import csv

def read_financial_operations(file_path):
    transactions = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return transactions


def test_read_financial_operations_success():
    mock_csv_data = "date,amount,description\n2023-01-01,100,Salary\n2023-01-02,-50,Groceries\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        result = read_financial_operations("mocked_file.csv")
        expected_result = [
            {'date': '2023-01-01', 'amount': '100', 'description': 'Salary'},
            {'date': '2023-01-02', 'amount': '-50', 'description': 'Groceries'}
        ]
        assert result == expected_result

def test_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_financial_operations("non_existent_file.csv")
        assert result == []

def test_other_exception():
    with patch("builtins.open", side_effect=Exception("Some error")):
        result = read_financial_operations("mocked_file.csv")
        assert result == []
