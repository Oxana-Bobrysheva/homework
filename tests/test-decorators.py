import pytest
from src.decorators import log
from src.widget import mask_account_card, get_date


# Тест для успешного выполнения функции
def test_log_success(capsys):
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
