from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """Function that takes the string with card name or account
    and gives back masked string of digits and stars."""
    if "счет" in card_or_account_info.lower():
        result = str(get_mask_account(card_or_account_info[-20:]))
    else:
        result = str(get_mask_card_number(card_or_account_info[-16:]))
    return result


def get_date(date_line: str) -> str:
    """Function that turns the line with full date information
    into the date as in the example (day.month.year)."""
    right_date = str(date_line[8:10] + "." + date_line[5:7] + "." + date_line[:4])
    return right_date


result = mask_account_card("Visa Platinum 7000792289606361")
print(result)
print(get_date("2024-03-11T02:26:18.671407"))
