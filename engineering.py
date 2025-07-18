"""
Название модуля: engineering.py

Описание:
    Запускает программу.

Функции:
    - main(): отвечает за импорт и иницилизацию

"""

from core.parameters import get_wall_size, get_brick_type, get_mortar_type, save_in_file
from core.calculate import (
    get_wall_volume,
    get_brick_volume,
    get_brick_with_mortar_volume,
    get_brick_count,
    get_stock_ratio,
    get_rounding_up,
)


def main():
    length, height, thickness = get_wall_size()
    brick_length, brick_width, brick_height = get_brick_type()
    mortar = get_mortar_type()

    wall_volume = get_wall_volume(length, height, thickness)
    brick_volume = get_brick_volume(
        brick_length, brick_width, brick_height
    )  
    brick_and_mortar_volume = get_brick_with_mortar_volume(
        brick_length, brick_width, brick_height, mortar
    )
    brick_count = get_brick_count(wall_volume, brick_and_mortar_volume)
    stock = get_stock_ratio(brick_count)
    finish = get_rounding_up(brick_count)
    finish_coefficient = get_rounding_up(stock)

    result: list[str] =[
        f"Объем стены: {wall_volume:.2f} м³\n",
        f"Объем одного кирпича: {brick_volume:.6f} м³\n",
        f"Объем одного кирпича с раствором: {brick_and_mortar_volume:.6f} м³\n",
        f"Необходимое количество кирпичей: {brick_count:.2f} шт\n",
        f"С учетом запаса: {stock:.2f} шт\n",
        f"Итоговое количество кирпичей (округлено): {finish} шт\n",
        f"Итоговое количество кирпичей с запасом (округлено): {finish_coefficient} шт\n"]
    
    save_in_file(result)
    print("Отчёт загружен в файл save.txt")

if __name__ == "__main__":
    main()
