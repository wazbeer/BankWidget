import json
import logging
import os

log_path = os.path.join("..", "logs", "utils.log")
utils_logger = logging.getLogger(__name__)

file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
utils_logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler.setFormatter(formatter)
utils_logger.addHandler(file_handler)


def get_financial_transactions(path: str) -> list[dict]:
    """Функция принимает Json фпйл и возвращает в python читаемый словарь"""
    utils_logger.info(f"Transactions acquiring attempt from '{path}'")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            utils_logger.info(f"Loaded JSON from '{path}'")

        if isinstance(data, list):
            utils_logger.info(f"Successfully acquired transaction list from '{path}'")
            return data

        utils_logger.error(f"'{path}' is not a list")
        return []

    except (FileNotFoundError, json.JSONDecodeError) as e:
        utils_logger.error(f"Error handling file '{path}': {e}")
        return []
