import logging
import os

log_path = os.path.join("..", "logs", "masks.log")
mask_logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
mask_logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler.setFormatter(formatter)
mask_logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    mask_logger.info(f"Card mask attempt '{card_number}'")

    if card_number is str:
        masked = card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:16]
        mask_logger.info(f"Successful card mask attempt '{card_number}'")
        return masked
    else:
        mask_logger.error(f"Failed card mask attempt '{card_number}'")
        return ""


def get_mask_account(card_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    mask_logger.info(f"Account mask attempt '{card_number}'")

    if card_number is str:
        masked = "**" + card_number[-4:]
        mask_logger.info(f"Successful account mask attempt '{card_number}'")
        return masked
    else:
        mask_logger.error(f"Failed account mask attempt '{card_number}'")
        return ""


if __name__ == "__main__":
    print(get_mask_card_number("1234567891234567"))
