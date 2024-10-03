from src.masks import get_mask_card_number

def test_get_mask_card_number():
    assert get_mask_card_number('1234567812345678') == '1234 56** **** 5678'
    assert get_mask_card_number('') == 'This card number is NOT correct. It should have 16 numbers. Try again.'