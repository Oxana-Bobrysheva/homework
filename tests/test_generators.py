import unittest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


class TestTransactionsModule(unittest.TestCase):

    def setUp(self):
        """Подготовка данных для тестов"""
        self.transactions = [
            {"description": "Transaction 1", "operationAmount_currency_code": "USD"},
            {"description": "Transaction 2", "currency_code": "EUR"},
            {"description": "Transaction 3", "operationAmount_currency_code": "USD"},
            {"description": "Transaction 4", "currency_code": "GBP"},
        ]

    def test_filter_by_currency(self):
        """Тестирование функции filter_by_currency"""
        filtered_transactions = filter_by_currency(self.transactions, "USD")
        self.assertEqual(len(filtered_transactions), 2)
        self.assertEqual(filtered_transactions[0]["description"], "Transaction 1")
        self.assertEqual(filtered_transactions[1]["description"], "Transaction 3")

        # Тест на отсутствие совпадений
        filtered_transactions_empty = filter_by_currency(self.transactions, "JPY")
        self.assertEqual(filtered_transactions_empty, [])

    def test_transaction_descriptions(self):
        """Тестирование функции transaction_descriptions"""
        descriptions = list(transaction_descriptions(self.transactions))
        self.assertEqual(len(descriptions), 4)
        self.assertIn("Transaction 1", descriptions)
        self.assertIn("Transaction 2", descriptions)

    def test_card_number_generator(self):
        """Тестирование функции card_number_generator"""
        generated_cards = list(card_number_generator(0, 5))  # Генерируем 5 карт
        expected_cards = [
            "0000 0000 0000 0000",
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
        ]
        self.assertEqual(generated_cards, expected_cards)


if __name__ == "__main__":
    unittest.main()
