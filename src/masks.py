def get_mask_card_number(card_number: str) -> str:
    """Function that takes card number and turns it into the mask
    as in example XXXX XX** **** XXXX."""
    if len(card_number) == 16:
        part1 = card_number[:4]
        part2 = card_number[4:6]
        part3 = card_number[-4:]
        mask_card_number = part1 + " " + part2 + "** **** " + part3
        return mask_card_number
    else:
        return "This card number is NOT correct. It should have 16 numbers. Try again."

def get_mask_account(account_number: str) -> str:
    """Function that takes account number and turns it into the mask
    as in example **XXXX."""
    mask_account = "**" + account_number[-4:]
    return mask_account
