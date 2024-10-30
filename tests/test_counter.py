import unittest
from src.counter import get_categories, count_transactions_by_category

class TestCounterFunctions(unittest.TestCase):

    def test_get_categories(self):
        # Тестируем функцию get_categories
        transactions = [
            {"description": "Groceries"},
            {"description": "Utilities"},
            {"description": "Groceries"},
            {"description": None},
            {"description": "Entertainment"},
        ]

        expected_categories = ["Groceries", "Utilities", "Entertainment"]
        result = get_categories(transactions)

        # Проверяем, что результат содержит все ожидаемые категории
        self.assertTrue(set(expected_categories).issubset(set(result)))
        # Проверяем, что результат не содержит дубликатов
        self.assertEqual(len(result), len(set(result)))

    def test_count_transactions_by_category(self):
        # Тестируем функцию count_transactions_by_category
        transactions = [
            {"description": "Groceries at Store"},
            {"description": "Utilities payment"},
            {"description": "Groceries"},
            {"description": "Entertainment - Movie"},
            {"description": "Groceries shopping"},
        ]

        categories = ["Groceries", "Utilities", "Entertainment"]
        expected_count = {
            "Groceries": 3,
            "Utilities": 1,
            "Entertainment": 1,
        }

        result = count_transactions_by_category(transactions, categories)

        # Проверяем, что результат соответствует ожидаемому
        self.assertEqual(result, expected_count)

    def test_count_transactions_by_category_no_matches(self):
        # Тестируем случай, когда нет совпадений категорий
        transactions = [
            {"description": "Rent payment"},
            {"description": "Gym membership"},
        ]

        categories = ["Groceries", "Utilities", "Entertainment"]
        expected_count = {}

        result = count_transactions_by_category(transactions, categories)

        # Проверяем, что результат соответствует ожидаемому
        self.assertEqual(result, expected_count)

if __name__ == '__main__':
    unittest.main()
