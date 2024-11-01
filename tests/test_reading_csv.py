import unittest
from unittest.mock import mock_open, patch

from src.reading_csv import read_financial_operations


class TestReadFinancialOperations(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="column1;column2\nvalue1;value2\nvalue3;value4\n")
    def test_read_financial_operations_success(self, mock_file):
        expected_result = [{"column1": "value1", "column2": "value2"}, {"column1": "value3", "column2": "value4"}]
        result = read_financial_operations("dummy_path.csv")
        self.assertEqual(result, expected_result)
        mock_file.assert_called_once_with("dummy_path.csv", mode="r", encoding="utf-8")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_financial_operations_file_not_found(self, mock_file):
        result = read_financial_operations("non_existent_file.csv")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("non_existent_file.csv", mode="r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open)
    def test_read_financial_operations_other_exception(self, mock_file):
        mock_file.side_effect = Exception("Some error")
        result = read_financial_operations("dummy_path.csv")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("dummy_path.csv", mode="r", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
