"""
Название модуля: masonry.py

Описание:
    Здесь находятся основные классы и методы для рассчётов

Классы:
    Wall -класс для расчёта стен
    Brick - класс для расчёта кирпича
    Calculator - класс для общего расчёта
"""
COEFFICIENT = 1.1
THOUSAND = 1000
MILLION = 1_000_000
BILLION = 1_000_000_000

class Wall():
    # Тип кладки и его толщина. Можно расширить
    masonry_types = {
        1: ("В половину кирпича", 0.12),
        2: ("В один кирпич", 0.25),
        3: ("В полтора кирпича", 0.38),
        4: ("В два кирпича", 0.51),
        5: ("В два с половиной кирпича", 0.64),
        6: ("В три кирпича", 0.77),
    }
    # По дефолту у всего размеры 1. Также есть список с кортежами, в которую нужно добавить ширину и высоту (для проемов)
    def __init__(self, *, length: float=1, height: float=1, type_id: int=1, openings: list[tuple[float, float]] = [], lintels: list[tuple[float, float]] = []) -> None: # = None или []?
        # Тернарный оператор. Проверяем, чтобы значения не были ноль
        # Вдруг кто-то захочет ввести ноль - будет ноль
        self.length = length if length > 0 else 1 
        self.height = height if height > 0 else 1
        self.masonry_names, self.thickness = self.masonry_types.get(type_id, ("В один кирпич", 0.25)) # get стандартный метод словаря
        self.openings = openings or [] # Поле для списка. Пустое, если проемов нет.
        self.lintels = lintels or [] # Перемычка

    def square(self) -> float: # площадь стены (лицевая сторона)
        return self.length * self.height

    def volume(self) -> float:
        # (Площадь всей стены - площадь проемов) * толщина - объем перемычки
        return (self.square() - self.get_openings_area())* self.thickness - self.get_lintels_volume()# Объем стены (толщина из списка)
    
    def get_openings_area(self) -> float: # Запрашиваем площадь проемов
        return sum(width * height for width, height in self.openings) # складываем каждую площадь из списка

    def get_openings_volume(self) -> float: # Объем проема
        return self.get_openings_area() * self.thickness # Просто умножаем площадь на толщину кладки

    def get_lintels_volume(self) -> float:
        return sum(length * height * self.thickness for length, height in self.lintels)


class Brick: 
    # Список из типа кирпичей. Можно расширить
    brick_types = {
        1: ("Одинарный кирпич (1НФ)", 250, 120, 65),
        2: ("Полуторный кирпич (1.4НФ)", 250, 120, 88),
        3: ("Двойной кирпич (2.1НФ)", 250, 120, 138),
    }
    # Список из типа шва (как кладут раствор)
    mortar_types = {
        1: ("Тонкий шов", 8),
        2: ("Стандартный шов", 10),
        3: ("Утолщённый шов", 12),
        4: ("Очень толстый шов", 15),
    }
    # Создаем кирпич. По дефолту одинарный кирпич и стандартный шов
    def __init__(self, *,brick_id: int=1, mortar_id: int=2) -> None:
        self.brick_name, self.length, self.width, self.height = self.brick_types.get(brick_id, ("Одинарный кирпич (1НФ)", 250, 120, 65)) # раскрываем список
        self.mortar_name, self.mortar = self.mortar_types.get(mortar_id, ("Стандартный шов", 10)) # раскрываме ещё один список

    def volume(self) -> float: # Получаем объем кирпича. Делим на тысячу, чтобы перевести в кубометры. Или можно разделить на миллиард в конце
        return (self.length / THOUSAND) * (self.width / THOUSAND) * (self.height / THOUSAND)
    
    def brick_mortar_volume(self) -> float: # Получаем объем кирпича вместе с раствором
        l = (self.length + self.mortar) / THOUSAND 
        w = (self.width + self.mortar) / THOUSAND # Делим всё на тысячу, чтобы перевести в кубометры. Или на миллиард в конце
        h = (self.height + self.mortar) / THOUSAND
        return  l * w * h # Возвращаем объем
    
    def get_price(self, price_per_brick: float, total_bricks: float) -> float: # Получить цену кирпича
        return price_per_brick * total_bricks # Цена и количество кирпичей.
    # Можно присвоить в переменную количество кирпичей и поставить её в аргумент для этого метода, когда вы будете писать скрипт.

class Calculator:
    def __init__(self, *, wall: Wall, brick: Brick) -> None:
        self.wall = wall # Создаем объект класса Wall внутри Calculator
        self.brick = brick # Создаем объект класса Brick внутри Calculator

    def get_total_bricks(self, with_mortar: bool=True, with_coefficient: bool=True) -> float: # Считаем общее количество кирпичей
        wall_volume = self.wall.volume() # В поле wall_volume передаем объем от объекта wall, рассчитанного методом volume, от класса Wall!

        if with_mortar: # С раствором?  Да
            brick_volume = self.brick.brick_mortar_volume()
        else: # Нет, без раствора, пожалуйста
            brick_volume = self.brick.volume() # Этот метод volume - от класса Bricl!
        
        if with_coefficient: # С коэффициентом запаса считать? 
            return (wall_volume / brick_volume) * COEFFICIENT # Да
        return wall_volume / brick_volume # Без

    def get_mortar_volume(self): # Объем раствора
            return self.get_total_bricks() * (self.brick.brick_mortar_volume() - self.brick.volume()) # Все кирпичи * (объем кирпича с раствором - объем кирпича)

    def get_mortar_cost(self, price_per_m3: float) -> float: # Цена раствора 
        return self.get_mortar_volume() * price_per_m3 #объем раствора (предыдущий метод) * цена (ввести в аргумент метода)
    
    def get_total_cost(self, price_per_brick: float, price_per_m3: float) -> float: # общая цена кладки
        total_bricks = self.get_total_bricks() # Сохраняем в поле количество кирпичей
        cost_bricks = self.brick.get_price(price_per_brick, total_bricks) # получить цену кирпича (цена за кирпич * все кирпичи)
        cost_mortar = self.get_mortar_cost(price_per_m3) # Цена за кубометр раствора
        return cost_bricks + cost_mortar # Складываем цену за кирпич и цену за раствор

    def get_summary(self, *, price_per_brick: float| int | None = None, price_per_m3: float | int| None = None) -> str: # Для вывода всего.
        summary: list[str] = [] # пустой лист
        summary.append(f"Тип кладки: {self.brick.brick_name}") # добавляем имя кирпича (обращаемся к полю объекта brick)
        summary.append(f"Размер стены: {self.wall.length}м x {self.wall.height}м") # Длина и ширина к объекту в calc
        summary.append(f"Тип кладки: {self.wall.masonry_names} ({self.wall.thickness} м)") # Имя и толщина (к полю объекта wall)
        summary.append(f"Объём стены: {round(self.wall.volume(), 3)} м³") # Объем, используем метод volume из wall

        total_bricks = self.get_total_bricks() # сохраняем в поле общее количество кирпичей
        summary.append(f"Кирпичей нужно: {int(total_bricks)} шт") # Добавляем в список общее количество кирпичей

        mortar_vol = self.get_mortar_volume() # сохраняем в поле объем раствора
        summary.append(f"Объём раствора: {round(mortar_vol, 3)} м³") # Добавляем в список

        if price_per_brick is not None: # Если не забыли указать цену за один кирпич
            brick_cost: float = total_bricks * price_per_brick # Считаем общую цену
            summary.append(f"Стоимость кирпичей: {round(brick_cost, 2)} ₽") # Добавляем в спиоск

        if price_per_m3 is not None: # Если не забыли указать цену за кубометр раствора
            mortar_cost: float = mortar_vol * price_per_m3 # Получаем цену
            summary.append(f"Стоимость раствора: {round(mortar_cost, 2)} ₽") # Добавляем в список

        if price_per_brick is not None and price_per_m3 is not None: # А если указали цену за кирпич и объем раствора одновременно? Вау!
            total_cost: float = brick_cost + mortar_cost # type: ignore # Это для аннотации, чтобы пайтон не ругался
            summary.append(f"Общая стоимость кладки: {round(total_cost, 2)} ₽") # type: ignore # Это для аннотации, чтобы пайтон не ругался

        return "\n".join(summary) # Возвращаем список в виде строки
