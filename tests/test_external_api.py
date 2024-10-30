import unittest
from unittest.mock import patch, Mock
from src.external_api import exchange_currency

class TestExchangeCurrency(unittest.TestCase):

    @patch('src.external_api.requests.get')
    def test_exchange_currency_rub_to_other(self, mock_get):
        # Настраиваем мок для ответа API
        transaction = {
            "operationAmount": {
                "amount": 1000,
                "currency": {"code": "USD"}
            }
        }

        # Настраиваем мок ответа
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 75000}  # Предположим, что 1000 USD = 75000 RUB
        mock_get.return_value = mock_response

        # Вызываем тестируемую функцию
        result = exchange_currency(transaction)

        # Проверяем, что результат соответствует ожиданиям
        self.assertEqual(result, 75000)
        mock_get.assert_called_once()  # Проверяем, что запрос был выполнен

    @patch('src.external_api.requests.get')
    def test_exchange_currency_rub_to_rub(self, mock_get):
        transaction = {
            "operationAmount": {
                "amount": 1000,
                "currency": {"code": "RUB"}
            }
        }

        result = exchange_currency(transaction)

        # Проверяем, что результат равен 1000
        self.assertEqual(result, 1000)
        mock_get.assert_not_called()  # Запрос не должен быть выполнен

    @patch('src.external_api.requests.get')
    def test_exchange_currency_api_error(self, mock_get):
        transaction = {
            "operationAmount": {
                "amount": 1000,
                "currency": {"code": "USD"}
            }
        }

        # Настраиваем мок ответа на ошибку
        mock_response = Mock()
        mock_response.status_code = 404  # Ошибка 404
        mock_get.return_value = mock_response

        result = exchange_currency(transaction)

        # Проверяем, что результат равен None
        self.assertIsNone(result)
        mock_get.assert_called_once()  # Проверяем, что запрос был выполнен

if __name__ == '__main__':
    unittest.main()

