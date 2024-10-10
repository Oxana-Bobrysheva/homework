from functools import wraps


def log(filename=None):
    """Function decorator that allows to write the process of execution of the function
    into the log file or a console."""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok \n")
                else:
                    print(f"{func.__name__} ok")
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ERROR: {e.__class__.__name__}. Inputs: {args}, {kwargs} \n")
                else:
                    print(f"{func.__name__} ERROR: {e.__class__.__name__}. Inputs: {args}, {kwargs}")

        return inner

    return wrapper
