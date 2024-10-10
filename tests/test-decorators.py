from src.decorators import log


# Тест для успешного выполнения функции
def test_log_success(capsys):
    @log()
    def faulty_function(x, y):
        return x / y

    faulty_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "faulty_function ok\n"


# Тест для обработки исключений
def test_log_error(capsys):
    @log()
    def faulty_function(x, y):
        return x / y

    faulty_function(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "faulty_function ERROR: ZeroDivisionError. Inputs: (2, 0), {}\n"
