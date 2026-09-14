def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    masked = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:16]

    return masked


def get_mask_account(card_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""

    masked = "**" + card_number[-4:]

    return masked


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
