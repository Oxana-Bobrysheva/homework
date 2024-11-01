import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("/home/user/PycharmProjects/homework_new/logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Function that takes card number and turns it into the mask
    as in example XXXX XX** **** XXXX."""
    logger.info("Starting the function get_mask_card_number")

    if not isinstance(card_number, str):
        raise TypeError("Expected a string")

    if len(card_number) == 16 and card_number.isdigit():
        part1 = card_number[:4]
        part2 = card_number[4:6]
        part3 = card_number[-4:]
        mask_card_number = f"{part1} {part2}** **** {part3}"
        logger.info(f"Mask of the credit card was made: {mask_card_number}")
        return mask_card_number
    else:
        logger.warning("This card number is NOT correct.")
        return "This card number is NOT correct. It should have 16 numbers. Try again."


def get_mask_account(account_number: str) -> str:
    """Function that takes account number and turns it into the mask
    as in example **XXXX."""
    logger.info("Starting the function get_mask_account")

    if not isinstance(account_number, str):
        raise TypeError("Expected a string")

    account_number = account_number.replace(" ", "")
    if len(account_number) == 20 and account_number.isdigit():
        mask_account = "**" + account_number[-4:]
        logger.info(f"Mask of the account was made: {mask_account}")
        return mask_account
    else:
        logger.warning("This card number is NOT correct.")
        return "This account number is NOT correct. It should have 20 numbers. Try again."


if __name__ == "__main__":
    print(get_mask_card_number("1234567812345677"))
    print(get_mask_account("12345123451234512344"))
