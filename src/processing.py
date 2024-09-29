def filter_by_state(cards_information: list, state: str = "EXECUTED") -> list:
    """Function that takes the list of dictionaries and returns a new list
    of only those dictionaries in which the key "state" matches the indicated value.
    """
    filtered_list = []
    for card_information in cards_information:
        if card_information["state"] == state:
            filtered_list.append(card_information)
    return filtered_list


def sort_by_date(cards_information: list, reverse: bool = True) -> list:
    """Function that takes the list of dictionaries and returns the sorted list
    of  dictionaries by date."""
    sorted_list_of_dictionaries = sorted(cards_information, key=lambda x: x["date"], reverse = reverse)
    return sorted_list_of_dictionaries

# sorted_list_of_dictionaries = [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
# print(sort_by_date(sorted_list_of_dictionaries, False))


# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
