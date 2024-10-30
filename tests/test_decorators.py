import unittest
from unittest.mock import patch

from src.decorators import log


class TestLogDecorator(unittest.TestCase):

    @patch("src.decorators.logging.info")
    @patch("src.decorators.logging.error")
    def test_log_success(self, mock_error, mock_info):
        @log()
        def sample_function(x, y):
            return x + y

        result = sample_function(2, 3)

        # Проверяем, что результат функции правильный
        self.assertEqual(result, 5)

        # Проверяем, что логирование вызвано корректно
        mock_info.assert_any_call("Starting 'sample_function' with arguments: (2, 3), {}")
        mock_info.assert_any_call("'sample_function' returned: 5")
        mock_info.assert_any_call("Finished 'sample_function'")

        # Проверяем, что лог ошибок не был вызван
        mock_error.assert_not_called()

    @patch("src.decorators.logging.info")
    @patch("src.decorators.logging.error")
    def test_log_error(self, mock_error, mock_info):
        @log()
        def sample_function(x, y):
            return x / y

        with self.assertRaises(ZeroDivisionError):
            sample_function(1, 0)

        # Проверяем, что логирование вызвано корректно
        mock_info.assert_any_call("Starting 'sample_function' with arguments: (1, 0), {}")
        mock_error.assert_any_call(
            "Error in 'sample_function': ZeroDivisionError - division by zero with arguments: (1, 0), {}"
        )
        mock_info.assert_any_call("Finished 'sample_function'")


if __name__ == "__main__":
    unittest.main()
