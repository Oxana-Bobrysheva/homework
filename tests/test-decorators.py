import pytest

from src.decorators import log
from src.widget import get_date, mask_account_card


# Тест для успешного выполнения функции
def test_log_success(capsys):
    """Testing function that checks decorator."""
    result = mask_account_card("Visa 1234567812345678")
    assert result == None

    captured = capsys.readouterr()
    assert "mask_account_card ok\n" in captured.out


# Тест для обработки исключений
def test_log_error(capsys):
    @log()
    def faulty_function(x, y):
        return x / y

    faulty_function(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "faulty_function ERROR: ZeroDivisionError. Inputs: (2, 0), {}\n"
