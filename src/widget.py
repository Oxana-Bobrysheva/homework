from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """Function that takes the string with card name or account
    and gives back masked string of digits and stars."""
    if len(card_or_account_info) < 16:
        return "Wrong input! Try again."
    elif sum(char.isdigit() for char in card_or_account_info) == 20 and "счет" in card_or_account_info.lower():
        result = str(get_mask_account(card_or_account_info[-20:]))
    elif sum(char.isdigit() for char in card_or_account_info) == 20:
        result = str(get_mask_account(card_or_account_info))
    elif sum(char.isdigit() for char in card_or_account_info) < 20 and "счет" in card_or_account_info.lower():
        result = "Wrong input! Try again."
    elif sum(char.isdigit() for char in card_or_account_info) == 16:
        result = str(get_mask_card_number(card_or_account_info[-16:]))
    else:
        return "Wrong input! Try again."
    return result


def get_date(date_line: str) -> str:
    """Function that turns the line with full date information
    into the date as in the example (day.month.year)."""
    if date_line == "":
        return "No date information"
    else:
        right_date = str(date_line[8:10] + "." + date_line[5:7] + "." + date_line[:4])
        return right_date
