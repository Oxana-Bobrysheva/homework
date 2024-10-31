from .masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """Function that takes the string with card name or account
    and gives back masked string of digits and stars."""

    # Проверка на пустую строку
    if not card_or_account_info:
        pass

    digit_count = sum(char.isdigit() for char in card_or_account_info)

    # Проверка на минимальную длину
    if len(card_or_account_info) < 16:
        return "Wrong input! Try again."

    # Обработка счета
    if digit_count == 20 and "счет" in card_or_account_info.lower():
        return str(get_mask_account(card_or_account_info[-20:]))

    # Обработка обычного номера с 20 цифрами
    elif digit_count == 20:
        return str(get_mask_account(card_or_account_info))

    # Проверка на некорректный счет
    elif digit_count < 20 and "счет" in card_or_account_info.lower():
        return "Wrong input! Try again."

    # Обработка кредитной карты
    elif digit_count == 16:
        return str(get_mask_card_number(card_or_account_info[-16:]))

    # Если ничего не подошло
    return "Wrong input! Try again."


def get_date(date_line: str) -> str:
    """Function that turns the line with full date information
    into the date as in the example (day.month.year)."""
    if date_line == "":
        return "No date information"
    else:
        right_date = str(date_line[8:10] + "." + date_line[5:7] + "." + date_line[:4])
        return right_date
