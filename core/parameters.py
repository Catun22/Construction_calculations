"""
Название модуля: parameters.py

Описание:
    Собирает и валидирует параметры, необходимые для расчётов кладки:
        - Размеры стены
        - Толщина раствора
        - Тип кирпича

Функции:
    - get_wall_size(): отвечает за размеры стены
    - get_mortar_type(): отвечает за тип раствора
    - get_brick_type(): отвечает за тип кирпича
"""

import lib.convert as convert
import lib.gost_data_base as gdb
from lib.validator import entry_validation

masonry_tuple = gdb.masonry_wall_type
mortar_tuple = gdb.mortar_thickness_type
brick_tuple = gdb.brick_type


def get_wall_size() -> tuple[int, int, int]:
    """Запрашивает у пользователя размер стены и возвращает кортеж.

    Функция запрашивает по-очереди длину и высоту стены.
    Толщину стены пользователь может выбрать. По стандарту: 1.
    Производит валидацию введеных значений, чтобы убедиться, что пользователь
    ввел положительные целые числа.
    Returns:
        tuple[int,int,int]: Длина, высота, толщина.
    """
    length = entry_validation("Введите длину стены (м): ")
    height = entry_validation("Введите высоту стены (м): ")
    thickness: int = convert.get_variants_from_tuple(masonry_tuple)
    print(f"Выбранная толщина стены: {thickness} мм")

    return length, height, thickness


def get_mortar_type() -> int:
    """Запрашивает у пользователя толщину раствора и возвращает целое число.

    Функция запрашивает толщину раствора для кладки.
    Толщину раствора пользователь может выбрать.
    По стандарту реокмендуется использовать значение 10.
    Производит валидацию введеных значений, чтобы убедиться, что пользователь
    ввел положительные целые числа.
    Returns:
        int: Толщина раствора.
    """
    thickness: int = convert.get_variants_from_tuple(mortar_tuple)
    print(f"Выбранная толщина раствора: {thickness} мм")
    return thickness


def get_brick_type() -> tuple[int, int, int]:
    """Запрашивает у пользователя тип кирпича и возвращает кортеж.

    Функция запрашивает тип кирпича для кладки.
    Тип кирпича пользователь может выбрать.
    По стандарту рекомендуется использовать "Одинарный кирпич"
    Производит валидацию введеных значений, чтобы убедиться, что пользователь
    ввел положительные целые числа.
    Returns:
        tuple[int, int, int]: Размер кирпича.
    """
    brick: tuple[int, int, int] = convert.get_variants_from_tuple(brick_tuple)
    print(f"Размеры кирпича: {brick} мм")
    return brick


def save_in_file(data: list, /) -> None:
    with open("save.txt", "a", encoding="UTF-8") as f:
        print()
        for item in data:
            f.write(item)
        f.write("\n")
