import logging
from functools import wraps


def log(filename=None):
    # Настройка логирования
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f"Starting '{func.__name__}' with arguments: {args}, {kwargs}")
            try:
                result = func(*args, **kwargs)
                logging.info(f"'{func.__name__}' returned: {result}")
                return result
            except Exception as e:
                logging.error(f"Error in '{func.__name__}': {type(e).__name__} - {e} with arguments: {args}, {kwargs}")
                raise  # Перебрасываем исключение дальше
            finally:
                logging.info(f"Finished '{func.__name__}'")

        return wrapper

    return decorator



