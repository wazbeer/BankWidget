# Виджет банковских операций (BankWidget)

## Описание
Виджет банковских операций — это бэкенд-сервис для личного кабинета клиента банка. Проект готовит и обрабатывает данные для отображения истории успешных и отмененных банковских транзакций, маскирует конфиденциальные данные (номера карт и счетов) и форматирует даты.

## Функционал

### 1. Модуль `masks` (`src/masks.py`)
* `get_mask_card_number(card_number)` — маскирует номер банковской карты по маске `XXXX XX** **** XXXX`.
* `get_mask_account(account_number)` — маскирует номер банковского счета по маске `**XXXX`.

### 2. Модуль `widget` (`src/widget.py`)
* `mask_account_card(data)` — определяет тип (карта или счет) и маскирует номер, сохраняя название (например, `Visa Platinum 7000 79** **** 6361`).
* `get_date(date_string)` — преобразует строку с датой из формата ISO в формат `ДД.ММ.ГГГГ` (например, `11.03.2024`).

### 3. Модуль `processing` (`src/processing.py`)
* `filter_by_state(operations, state='EXECUTED')` — фильтрует список банковских операций по статусу (`EXECUTED`, `CANCELED` и т.д.).
* `sort_by_date(operations, reverse=True)` — сортирует список операций по дате (по умолчанию — от самых свежих к старым).

## Установка

1. Клонируйте репозиторий:
git clone https://github.com/wazbeer/BankWidget.git
cd BankWidget
Установите зависимости через Poetry:

poetry install
Использование
Пример работы с модулем processing:

from src.processing import filter_by_state, sort_by_date

operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 2, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
]

# Фильтрация по статусу EXECUTED
executed_ops = filter_by_state(operations)

# Сортировка по дате
sorted_ops = sort_by_date(operations)
Проверка качества кода
Для проверки стиля кода и типизации используются линтеры:

poetry run flake8

poetry run mypy src

poetry run black --check src

poetry run isort --check src

## Тестирование

Проект покрыт автотестами с использованием `pytest`.

Для запуска тестов выполните:

poetry run pytest