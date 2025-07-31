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

from tkinter import *  # type: ignore
from tkinter import messagebox

from core.masonry import Wall, Brick, Calculator
from lib.utilits import save_in_file, get_space  # type: ignore


class Interface:
    def __init__(self) -> None:
        # Создаем интерфейс
        self.window = Tk()
        self.window.title("РАСЧЁТЫ КЛАДКИ КИРПИЧА")
        self.window.geometry("1024x640")
        self.window.resizable(width=False, height=False)
        icon = PhotoImage(file="icons/fox_icon.png")
        self.window.iconphoto(True, icon)
        self.window.configure(bg="#010101")

        ################################################
        # Создаем контейнеры
        self.main_frame = Frame(self.window, bg="#010101")
        self.top_frame_1 = Frame(
            self.main_frame, bg="#010101", relief=RAISED, bd=10
        )  # Фрейм для типа кладки
        self.top_frame_2 = Frame(
            self.main_frame, bg="#010101", relief=RAISED, bd=10
        )  # Фрейм для типа кирпича
        self.top_frame_3 = Frame(
            self.main_frame, bg="#010101", relief=RAISED, bd=10
        )  # Фрейм для типа шва
        self.top_frame_4 = Frame(
            self.main_frame, bg="#010101", relief=RAISED, bd=10
        )  # Фрейм для ввода размеров стены и кирпича

        self.middle_frame = Frame(
            self.main_frame, bg="#010101", relief=RAISED, bd=10
        )  # Фрейм для всех кнопок

        ################################################
        # Для использвования с Radiobutton
        self.masonry_type_var = IntVar()  # Связь для радиокнопок
        self.brick_type_var = IntVar()  # Связь для радиокнопок
        self.mortar_type_var = IntVar()  # Связь для радиокнопок

        ################################################
        # Создаем кнопки для фрейма тип кладки
        self.label_1 = Label(
            self.top_frame_1,
            text="Тип кладки:",
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        self.rbtn_1 = Radiobutton(
            self.top_frame_1,
            text="В 0.5 кирпича (толщина 120 мм)",
            variable=self.masonry_type_var,
            value=1,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        self.rbtn_2 = Radiobutton(
            self.top_frame_1,
            text="В 1 кирпич (толщина 250 мм)",
            variable=self.masonry_type_var,
            value=2,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        self.rbtn_3 = Radiobutton(
            self.top_frame_1,
            text="В 1.5 кирпича (толщина 380 мм)",
            variable=self.masonry_type_var,
            value=3,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        self.rbtn_4 = Radiobutton(
            self.top_frame_1,
            text="В 2 кирпича (толщина 510 мм)",
            variable=self.masonry_type_var,
            value=4,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        self.rbtn_5 = Radiobutton(
            self.top_frame_1,
            text="В 3 кирпича (толщина 770 мм)",
            variable=self.masonry_type_var,
            value=5,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        # Инициализируем кнопки
        self.label_1.grid(row=0, sticky="n", pady=10)
        self.rbtn_1.grid(row=1, sticky="we", padx=20)
        self.rbtn_2.grid(row=2, sticky="we", padx=20)
        self.rbtn_3.grid(row=3, sticky="we", padx=20)
        self.rbtn_4.grid(row=4, sticky="we", padx=20)
        self.rbtn_5.grid(row=5, sticky="we", padx=20)

        ################################################
        # Создаем кнопки для фрейма тип кирпича
        self.label_2 = Label(
            self.top_frame_2,
            text="Тип кирпича:",
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        self.rbtn_6 = Radiobutton(
            self.top_frame_2,
            text="Одинарный (1НФ), (250x120x65)",
            variable=self.brick_type_var,
            value=1,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        self.rbtn_7 = Radiobutton(
            self.top_frame_2,
            text="Полуторный (1.4НФ), (250x120x88)",
            variable=self.brick_type_var,
            value=2,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        self.rbtn_8 = Radiobutton(
            self.top_frame_2,
            text="Двойной (2.1НФ), (250x120x138)",
            variable=self.brick_type_var,
            value=3,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        # Инициализируем кнопки
        self.label_2.grid(row=0, sticky="n", pady=10)
        self.rbtn_6.grid(row=1, sticky="we", padx=60)
        self.rbtn_7.grid(row=2, sticky="we", padx=60)
        self.rbtn_8.grid(row=3, sticky="we", padx=60)

        ################################################
        # Создаем кнопки для фрейма тип шва
        self.label_3 = Label(
            self.top_frame_3,
            text="Тип шва:",
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        self.rbtn_9 = Radiobutton(
            self.top_frame_3,
            text="Тонкий шов, (8 мм)",
            variable=self.mortar_type_var,
            value=1,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        self.rbtn_10 = Radiobutton(
            self.top_frame_3,
            text="Стандартный шов, (10 мм)",
            variable=self.mortar_type_var,
            value=2,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        self.rbtn_11 = Radiobutton(
            self.top_frame_3,
            text="Утолщённый шов, (12 мм)",
            variable=self.mortar_type_var,
            value=3,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        self.rbtn_12 = Radiobutton(
            self.top_frame_3,
            text="Очень толстый шов, (15 мм)",
            variable=self.mortar_type_var,
            value=4,
            bg="#010101",
            fg="#FFFFFF",
            activebackground="#010101",
            activeforeground="#FFFFFF",
            selectcolor="#353232",
            font=("Ink Free", 16),
            indicatoron=False,
        )
        # Инициализируем кнопки
        self.label_3.grid(row=0, sticky="n", pady=10)
        self.rbtn_9.grid(row=1, sticky="we", padx=50)
        self.rbtn_10.grid(row=2, sticky="we", padx=50)
        self.rbtn_11.grid(row=3, sticky="we", padx=50)
        self.rbtn_12.grid(row=4, sticky="we", padx=50)

        ################################################
        # Создаем лейблы и строки ввода для фрейма для ввода размеров
        self.label_4 = Label(
            self.top_frame_4,
            text="Длина стены:",
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        self.label_5 = Label(
            self.top_frame_4,
            text="Высота стены:",
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        self.label_6 = Label(
            self.top_frame_4,
            text="Ценза за кирпич:",
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        self.label_7 = Label(
            self.top_frame_4,
            text="Цена за м³ раствора:",
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        self.label_8 = Label(
            self.top_frame_4,
            text="Проемы (x,y),(x,y):",
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        self.label_9 = Label(
            self.top_frame_4,
            text="Перемычки (x,y),(x,y):",
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        self.entry_1 = Entry(self.top_frame_4, width=20, font=("Ink Free", 16))
        self.entry_2 = Entry(self.top_frame_4, width=20, font=("Ink Free", 16))
        self.entry_3 = Entry(self.top_frame_4, width=20, font=("Ink Free", 16))
        self.entry_4 = Entry(self.top_frame_4, width=20, font=("Ink Free", 16))
        self.entry_5 = Entry(self.top_frame_4, width=20, font=("Ink Free", 16))
        self.entry_6 = Entry(self.top_frame_4, width=20, font=("Ink Free", 16))

        # Инициализируем строки ввода
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.entry_3.grid(row=2, column=1)
        self.entry_4.grid(row=3, column=1)
        self.entry_5.grid(row=4, column=1)
        self.entry_6.grid(row=5, column=1)
        # Инициализируем лейблы
        self.label_4.grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.label_5.grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.label_6.grid(row=2, column=0, sticky="w", pady=5, padx=5)
        self.label_7.grid(row=3, column=0, sticky="w", pady=5, padx=5)
        self.label_8.grid(row=4, column=0, sticky="w", pady=5, padx=5)
        self.label_9.grid(row=5, column=0, sticky="w", pady=5, padx=5)

        ################################################
        # Создаем кнопки для фрейма с основными кнопками
        self.btn_1 = Button(
            self.middle_frame,
            text="Рассчитать",
            bg="#750000",
            fg="#FFFFFF",
            activebackground="#750000",
            activeforeground="#FFFFFF",
            font=("Ink Free", 16),
            width=14,
            command=self.calculate,
        )
        self.btn_2 = Button(
            self.middle_frame,
            text="Сохранить",
            bg="#750000",
            fg="#FFFFFF",
            activebackground="#750000",
            activeforeground="#FFFFFF",
            font=("Ink Free", 16),
            width=14,
            command=self.save,
        )
        self.btn_3 = Button(
            self.middle_frame,
            text="Нажми на меня",
            bg="#750000",
            fg="#FFFFFF",
            activebackground="#750000",
            activeforeground="#FFFFFF",
            font=("Ink Free", 16),
            width=14,
            command=self.joke,
        )
        self.btn_4 = Button(
            self.middle_frame,
            text="Выйти",
            bg="#750000",
            fg="#FFFFFF",
            activebackground="#750000",
            activeforeground="#FFFFFF",
            font=("Ink Free", 16),
            width=14,
            command=self.exit,
        )
        # Инициализируем кнопки
        self.btn_1.grid(row=0, column=0, sticky="w", padx=14, pady=5)
        self.btn_2.grid(row=0, column=1, sticky="w", padx=14, pady=5)
        self.btn_3.grid(row=0, column=2, sticky="w", padx=14, pady=5)
        self.btn_4.grid(row=0, column=3, sticky="w", padx=14, pady=5)

        ################################################
        # Расставляем фреймы в сетку
        self.main_frame.pack(expand=True)
        self.top_frame_1.grid(row=0, column=0, sticky="news")  # Фрейм для типа кладки
        self.top_frame_2.grid(row=0, column=1, sticky="news")  # Фрейм для типа кирпича
        self.top_frame_3.grid(row=1, column=0, sticky="news")  # Фрейм для типа шва
        self.top_frame_4.grid(
            row=1, column=1, sticky="news"
        )  # Фрейм для ввода размеров стены и кирпича
        self.middle_frame.grid(
            row=2, column=0, columnspan=2, sticky="news"
        )  # Фрейм для всех кнопок

    def calculate(self):

        openings: list[tuple[float, float]] = []
        lintels: list[tuple[float, float]] = []

        type_id = self.masonry_type_var.get()
        brick_id = self.brick_type_var.get()
        mortar_id = self.mortar_type_var.get()

        try:
            length = float(self.entry_1.get())
            height = float(self.entry_2.get())
            price_per_brick = float(self.entry_3.get())
            price_per_m3 = float(self.entry_4.get())
            openings_str = self.entry_5.get()
            lintels_str = self.entry_6.get()

            if "(" in openings_str and "," in openings_str:
                get_space(entry_text=openings_str, openings=openings)
            if "(" in lintels_str and "," in lintels_str:
                get_space(entry_text=lintels_str, openings=lintels)
        except ValueError:
            messagebox.showerror(
                title="Error", message="Ошибка. Введте корректные значения"
            )
            return

        wall = Wall(
            length=length,
            height=height,
            type_id=type_id,
            openings=openings,
            lintels=lintels,
        )
        brick = Brick(brick_id=brick_id, mortar_id=mortar_id)
        calc = Calculator(wall=wall, brick=brick)
        self.summary = calc.get_summary(
            price_per_brick=price_per_brick, price_per_m3=price_per_m3
        )

        self.new_window = Toplevel()
        self.new_window.title("РЕЗУЛЬТАТ")
        self.new_window.geometry("520x640")
        self.new_window.resizable(width=False, height=False)
        self.new_window.configure(bg="#010101")

        self.frame = Frame(self.new_window, bg="#010101")
        self.frame.pack(expand=True)

        self.label_result = Label(
            self.frame,
            text="Результаты расчёта",
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        self.label_result.pack()

        self.result_text = Text(
            self.frame,
            wrap="word",
            font=("Segoe UI", 12),
            bg="#010101",
            fg="#00FF00",
            insertbackground="white",
        )
        self.result_text.insert("1.0", self.summary)
        self.result_text.config(state="disabled")
        self.result_text.pack(expand=True, fill="both", padx=20, pady=10)

        self.button_save = Button(
            self.frame,
            text="Сохранить",
            bg="#750000",
            fg="#FFFFFF",
            activebackground="#750000",
            activeforeground="#FFFFFF",
            font=("Ink Free", 16),
            width=14,
            command=self.save,
        )
        self.button_save.pack()

    def save(self) -> None:
        save_in_file(self.summary)

    def joke(self):
        messagebox.showwarning(title="Спасибо", message="Спасибо, что нажал на меня")

    def exit(self):
        self.window.destroy()

    def start(self):
        self.window.mainloop()
