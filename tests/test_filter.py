import unittest
from unittest.mock import patch, Mock
from src.filter import filter_by_search_string
import re


class TestFilterBySearchString(unittest.TestCase):

    def setUp(self):
        """Метод, который выполняется перед каждым тестом."""
        self.transactions = [
            {"description": "Grocery shopping", "amount": 50.0},
            {"description": "Gas station", "amount": 30.0},
            {"description": "Online subscription", "amount": 15.0},
            {"description": "Dinner at restaurant", "amount": 75.0},
            {"description": "Electricity bill", "amount": 100.0},
        ]

    @patch('src.filter.re.compile')
    def test_filter_with_mocked_re_compile(self, mock_compile):
        """Тест с замокированной функцией re.compile."""
        # Настройка mock для возвращения объекта, который будет имитировать поведение search
        mock_pattern = Mock()
        mock_pattern.search.return_value = True  # Имитация успешного поиска
        mock_compile.return_value = mock_pattern

        # Выполнение теста
        result = filter_by_search_string(self.transactions, "Grocery")

        expected = self.transactions  # Все транзакции должны быть возвращены, так как search всегда True
        self.assertEqual(result, expected)

        # Проверка, что re.compile была вызвана с правильным аргументом
        mock_compile.assert_called_once_with("Grocery", re.IGNORECASE)

    @patch('src.filter.re.compile')
    def test_filter_no_match_with_mocked_re_compile(self, mock_compile):
        """Тест с замокированной функцией re.compile, возвращающей None."""
        mock_pattern = Mock()
        mock_pattern.search.return_value = None  # Имитация неудачного поиска
        mock_compile.return_value = mock_pattern

        # Выполнение теста
        result = filter_by_search_string(self.transactions, "Travel")

        expected = []  # Ожидаем пустой список, так как нет совпадений
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
