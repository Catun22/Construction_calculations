"""
Название модуля: convert.py

Описание:
    Содержит функцию для отображения и выбора значений из кортежа параметров.
    Используется при выборе типа кирпича, раствора или кладки.

Функции:
    - get_variants_from_tuple(): отвечает раскрытие кортежа и его возврат

"""

from lib.validator import entry_validation


def get_variants_from_tuple(
    massive: tuple[tuple[str, int | tuple[int, int, int]], ...], /
) -> int | tuple[int, int, int]:
    """Показывает список вариантов на выбор и возвращает соответствующее значение.

    Функция принимает кортеж с вариантами: имя и значение (int или кортеж из трёх int).
    Показывает их пользователю и возвращает значение, соответствующее выбору.

    Args:
        massive (tuple): Кортеж, содержащий пары (название, значение).

    Returns:
        int | tuple[int, int, int]: Выбранное значение — целое число или кортеж размеров.
    """
    print("Выберите вариант")
    for i, (name, value) in enumerate(massive, 1):

        if type(value) == int:
            print(f"{i}. {name} ({value} мм)")
        else:
            print(f"{i}. {name} ({' x '.join(map(str, value))} мм)")

    while True:
        choice = entry_validation("Введите номер варианта: ")
        if 1 <= choice <= len(massive):
            _, selected_value = massive[choice - 1]
            return selected_value
        else:
            print("Такого варианта нет.")
