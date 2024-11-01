import unittest
from unittest.mock import Mock, patch

from src.external_api import exchange_currency


class TestExchangeCurrency(unittest.TestCase):

    @patch("external_api.requests.get")
    def test_exchange_currency_success(self, mock_get):
        # Arrange
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}

        # Mock the response from the API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 7500}  # Assume 1 USD = 75 RUB
        mock_get.return_value = mock_response

        # Act
        result = exchange_currency(transaction)

        # Assert
        self.assertEqual(result, 7500)
        mock_get.assert_called_once()

    @patch("external_api.requests.get")
    def test_exchange_currency_rub(self, mock_get):
        # Arrange
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}

        # Act
        result = exchange_currency(transaction)

        # Assert
        self.assertEqual(result, 100.0)
        mock_get.assert_not_called()  # Ensure API was not called

    @patch("external_api.requests.get")
    def test_exchange_currency_api_error(self, mock_get):
        # Arrange
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "EUR"}}}

        # Mock the response from the API with an error status
        mock_response = Mock()
        mock_response.status_code = 400  # Bad Request
        mock_get.return_value = mock_response

        # Act
        result = exchange_currency(transaction)

        # Assert
        self.assertIsNone(result)
        mock_get.assert_called_once()

    @patch("external_api.requests.get")
    def test_exchange_currency_invalid_json(self, mock_get):
        # Arrange
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "GBP"}}}

        # Mock the response from the API with valid status but invalid JSON
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}  # No result key
        mock_get.return_value = mock_response

        # Act
        result = exchange_currency(transaction)

        # Assert
        self.assertIsNone(result)
        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
