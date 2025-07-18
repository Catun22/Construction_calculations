"""
Название модуля: calculate.py

Описание:
    Принимает данные и математические расчеты.

Функции:
    - get_wall_volume(): отвечает за объем стены
    - get_brick_montar_volume(): отвечает за объем кирпича с раствором
    - get_brick_count(): отвечает за количество кирпичей
    - get_stock_ratio(): отвечает за округление кирпичей
"""

from math import ceil

from lib.gost_data_base import COEFFICIENT, METERS_AND_MILI, CUBE_METERS_COEFFICIENT


def get_wall_volume(length: int, height: int, thickness: int, /) -> float:
    """Производит вычисление объема стены в метрах кубических

    Аргументы:
        length (int): Длина стены, м
        height (int): Высота стены, м
        thickness (int): Толщина стены, мм

    Возвращает:
        float: Объем стены, м³
    """
    return length * height * (thickness / METERS_AND_MILI)


def get_brick_volume(brick_l: int, brick_w: int, brick_h: int, /) -> float:
    """Производит вычисление объема кирпича без учета раствора

    Аргументы:
        brick_l (int): Длина кирпича, мм
        brick_w (int): Ширина кирпича, мм
        brick_h (int): Высота кирпича, мм

    Возвращает:
        float: Объем кирпича, м³
    """
    return (brick_l * brick_w * brick_h) / CUBE_METERS_COEFFICIENT


def get_brick_with_mortar_volume(
    length: int, width: int, height: int, mortar: int, /
) -> float:
    """Производит вычисление объема кирпича с учетом раствора

    Аргументы:
        length (int): Длина кирпича, мм
        width (int): Ширина кирпича, мм
        height (int): Высота кирпича, мм
        mortar (int): Толщина шва раствора, мм

    Возвращает:
        float: Объем кирпича с раствором, м³
    """
    return (
        (length + mortar) * (width + mortar) * (height + mortar)
    ) / CUBE_METERS_COEFFICIENT


def get_brick_count(wall_volume: float, brick_and_mortar_volume: float, /) -> float:
    """Вычисляет необходимое количество кирпичей

    Аргументы:
        wall_volume (float): Объем стены, м³
        brick_and_mortar_volume (float): Объем одного кирпича с раствором, м³

    Возвращает:
        float: Количество кирпичей
    """
    return wall_volume / brick_and_mortar_volume


def get_stock_ratio(brick_count: float, /) -> float:
    """Добавляет коэффициент запаса к количеству кирпичей

    Аргументы:
        brick_count (float): Количество кирпичей

    Возвращает:
        float: Количество кирпичей с учетом запаса
    """
    return brick_count * COEFFICIENT


def get_rounding_up(stock_ratio: float, /) -> int:
    """Округляет количество кирпичей вверх

    Аргументы:
        stock_ratio (float): Количество кирпичей (с запасом или без)

    Возвращает:
        int: Округленное количество кирпичей
    """
    return ceil(stock_ratio)
