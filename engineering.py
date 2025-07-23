"""
Название модуля: engineering.py

Описание:
    Запускает программу.

Функции:
    - main(): отвечает за импорт и иницилизацию
    - choose(): отвечает за выбор
    - get_openings() отвечает за проемы
    - save_in_file() отвечает за сохранение результата в файл
    - load() кастомный загрузчик
"""
import os
import sys
import time
import itertools

from lib.masonry import Wall, Brick, Calculator
from lib.validator import entry_validation, valid_openings


def main():

    spin = itertools.cycle("🌑"*1+"🌒"*1+"🌓"*1+"🌔"*1 +"🌕"*1+"🌖"*1+"🌗"*1+"🌘"*1)

    masonry_types = {
        1: "В половину кирпича",
        2: "В один кирпич",
        3: "В полтора кирпича",
        4: "В два кирпича",
        5: "В два с половиной кирпича",
        6: "В три кирпича",
    }
    brick_types = {
        1: "Одинарный (1НФ)",
        2: "Полуторный (1.4НФ)",
        3: "Двойной (2.1НФ)",
    }

    mortar_types = {
        1: "Тонкий шов",
        2: "Стандартный шов",
        3: "Утолщённый шов",
        4: "Очень толстый шов",
    }
    
    openings: list[tuple[float, float]] = []

    load(spin=spin) # type: ignore

    print("\nСТРОИТЕЛЬНЫЕ РАСЧЁТЫ КЛАДКИ КИРПИЧА\n")
    type_id = choose("Выберите тип кладки: ", masonry_types)
    length = float(entry_validation("Введите длину стены (метры):\n>> "))
    height = float(entry_validation("Введите высоту стены (метры):\n>> "))
    brick_id = choose("Выберите тип кирпича: ", brick_types)
    mortar_id = choose("Выберите тип шва: ", mortar_types)
    price_per_brick = float(entry_validation("Введите цену за 1 кирпич (₽):\n>> "))
    price_per_m3 = float(entry_validation("Введите цену за 1 м³ раствора:\n>> "))
    openings_count = valid_openings("Сколько проёмов (окна или двери)?\n>> ")
    get_openings(openings=openings, openings_count=openings_count)

    wall = Wall(length=length, height=height, type_id=type_id, openings=openings)
    brick = Brick(brick_id=brick_id, mortar_id=mortar_id)
    calc = Calculator(wall=wall, brick=brick)
    summary = calc.get_summary(
        price_per_brick=price_per_brick, price_per_m3=price_per_m3
    )
    print("\nРЕЗУЛЬТАТ:\n")
    print(summary)
    save_in_file(summary)


def choose(prompt: str, options: dict[int, str]) -> int:
    """Функция выбирает тип кирпича, кладки, шва"""
    while True:
        print(prompt)
        for key, value in options.items():
            print(f"{key}: {value}")  # type: ignore
        choise = entry_validation("Выберите вариант:\n>> ")
        if choise in options:
            return choise
        print("Неверный выбор, попробуйте снова.\n")


def get_openings(*, openings: list, openings_count: int) -> list[tuple[float, float]]:  # type: ignore
    """Функция берет данные по проемам у пользователя"""
    for i in range(openings_count):
        print(f"\nПроем номер {i+1}:")
        o_width = float(entry_validation("Введите ширину проема (метры): "))
        o_height = float(entry_validation("Введите высоту проема (метры): "))
        openings.append((o_width, o_height))  # type: ignore


def save_in_file(data: str, /) -> None:
    """Функция сохраняет в файл .txt"""
    with open("save.txt", "a", encoding="UTF-8") as f:
        print()
        f.write(data + "\n")

def load(*, spin: str):
    """Загрузчик"""
    is_windows = sys.platform.startswith("win")
    is_mac = sys.platform.startswith('darwin')
    is_linux = sys.platform.startswith('linux')

    clear_command = ""

    if is_windows:
        clear_command = "cls"
    elif is_mac:
        clear_command = "clear"
    elif is_linux:
        clear_command = "clear"
    else:
        print("Полный фунционал программы поддерживается только на: Linux, macOS, Windows.")

    os.system(clear_command)

    for i in range(101):
        sym = next(spin) # type: ignore
        print(f"\rЗагрузка: {i}% {sym}", end="", flush=True)
        time.sleep(0.1)
    print("\n")


if __name__ == "__main__":
    main()
