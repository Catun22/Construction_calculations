"""
Название модуля: validator.py

Описание:
    Собирает данные, напечатанные пользователем в input и проверяет на валидность.

Функци
    - entry_validation(prompt): Запрашивает числовое значение и проверяет его.
"""


def entry_validation(prompt: str, /) -> int:
    """Запрашивает у пользователя числовое значение и проверяет его валидность.

    Функция запрашивает ввод пользователя, преобразует его в целое число
    и проверяет значение. При неверном вводе повторяет запрос.

    Args:
        prompt (str): Сообщение, отоброжаемое пользователю при вооде
    Returns:
        int: Модуль числа, введеного пользователем
    """

    while True:
        try:
            value = float(input(prompt))

            if value != 0:
                return value # type: ignore
            elif value < 0:
                print("Ваше значение будет рассчитываться по модулю.")
                return abs(value) # type: ignore
            else:
                print("Введите число, отличное от нуля.")
    
        except ValueError:
            print("Введите численное значение")



def valid_openings(prompt: str, /)-> int:
    """Проверяет значение для проемов"""
    while True:
        try:
            value = int(input(prompt))

            if value >= 0:
                return value # type: ignore
            else:
                print("Введите число 0 или положительное число")
    
        except ValueError:
            print("Введите численное значение")
    
