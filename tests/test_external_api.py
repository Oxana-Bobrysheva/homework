import unittest
from unittest.mock import MagicMock, patch

from src.external_api import exchange_currency


class TestExchangeCurrency(unittest.TestCase):

    @patch("src.external_api.requests.get")  # Замените 'your_module' на имя Вашего модуля
    @patch("src.external_api.os.getenv")
    def test_exchange_currency_success(self, mock_getenv, mock_requests_get):
        # Настройка мока для API_TOKEN
        mock_getenv.return_value = "fake_api_token"

        # Настройка mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 100.0}
        mock_requests_get.return_value = mock_response

        # Вызов функции
        result = exchange_currency("USD", "RUB", 1000)

        # Проверка
        self.assertEqual(result, 100.0)
        mock_requests_get.assert_called_once()  # Убедитесь, что запрос был сделан один раз

    @patch("src.external_api.requests.get")
    @patch("src.external_api.os.getenv")
    def test_exchange_currency_failure(self, mock_getenv, mock_requests_get):
        # Настройка мока для API_TOKEN
        mock_getenv.return_value = "fake_api_token"

        # Настройка mock response для ошибки
        mock_response = MagicMock()
        mock_response.status_code = 404  # Симулируем ошибку 404
        mock_requests_get.return_value = mock_response

        # Вызов функции
        result = exchange_currency("USD", "RUB", 1000)

        # Проверка
        self.assertIsNone(result)  # Результат должен быть None в случае ошибки
        mock_requests_get.assert_called_once()  # Убедитесь, что запрос был сделан один раз

    @patch("src.external_api.requests.get")
    @patch("src.external_api.os.getenv")
    def test_exchange_currency_no_result(self, mock_getenv, mock_requests_get):
        # Настройка мока для API_TOKEN
        mock_getenv.return_value = "fake_api_token"

        # Настройка mock response с отсутствующим результатом
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_requests_get.return_value = mock_response

        # Вызов функции
        result = exchange_currency("USD", "RUB", 1000)

        # Проверка
        self.assertIsNone(result)  # Результат должен быть None, если нет 'result' в ответе
        mock_requests_get.assert_called_once()  # Убедитесь, что запрос был сделан один раз


if __name__ == "__main__":
    unittest.main()
