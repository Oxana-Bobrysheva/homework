import unittest
from unittest.mock import mock_open, patch

from src.utils import get_transactions


class TestGetTransactions(unittest.TestCase):

    @patch("os.path.isfile")
    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
    def test_get_transactions_valid_file(self, mock_file, mock_isfile):
        # Настроим mock для функции isfile
        mock_isfile.return_value = True

        result = get_transactions("operations.json")
        expected_result = [{"id": 1, "amount": 100}]
        self.assertEqual(result, expected_result)

    @patch("os.path.isfile")
    def test_get_transactions_file_not_found(self, mock_isfile):
        # Настроим mock для функции isfile
        mock_isfile.return_value = False

        result = get_transactions("operations.json")
        self.assertEqual(result, [])

    @patch("os.path.isfile")
    @patch("builtins.open", new_callable=mock_open, read_data="not a json")
    def test_get_transactions_invalid_json(self, mock_file, mock_isfile):
        # Настроим mock для функции isfile
        mock_isfile.return_value = True

        result = get_transactions("operations.json")
        self.assertEqual(result, [])

    @patch("os.path.isfile")
    @patch("builtins.open", new_callable=mock_open, read_data='{"not_a_list": true}')
    def test_get_transactions_not_a_list(self, mock_file, mock_isfile):
        # Настроим mock для функции isfile
        mock_isfile.return_value = True

        result = get_transactions("operations.json")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
