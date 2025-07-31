from tkinter import *  # type: ignore
from tkinter.ttk import *  # type: ignore
import time
import itertools


class Progress:
    # Создаем окно
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Download")
        icon = PhotoImage(file="icons/fox_icon.png")
        self.window.iconphoto(True, icon)
        self.window.geometry("560x240")
        self.window.resizable(False, False)

        self.download_status = False  # Флаг для оповещения успешного окончания

        # Добавляем прогресс-бар
        self.bar = Progressbar(self.window, orient=HORIZONTAL, length=300)
        self.bar.place(x=130, y=90)  # (ширина окна - размер бара)/2

        self.precent = StringVar()  # Связка
        self.status = StringVar()  # Связка
        # Создаем кнопочку
        Button(self.window, text="Download", command=self.starting).place(x=240, y=116)
        # Лейбл, который выводит проценты на экран
        Label(self.window, textvariable=self.precent, font=("Arial", 16)).place(
            x=430, y=88
        )  # х из бара + размер бара
        # Лейбл, который выводит "статутс" (текст)
        Label(
            self.window,
            textvariable=self.status,
            width=40,
            anchor="center",
            font=("Arial", 16),
        ).place(x=36, y=60)

    # Метод, который "двигает прогресс-бар"
    def starting(self):

        spin = itertools.cycle(
            "🌑" * 1
            + "🌒" * 1
            + "🌓" * 1
            + "🌔" * 1
            + "🌕" * 1
            + "🌖" * 1
            + "🌗" * 1
            + "🌘" * 1
        )

        words = [
            "Подключаюсь к спутнику...",
            "Анализирую..",
            "Взламываю Пентагон...",
            "Обновляю... 0/1000",
            "Перекур...",
            "Скачиваю...",
        ]
        for i in words:
            self.status.set(i)
            time.sleep(2)
            self.window.update_idletasks()
        x = 100
        for i in range(1, x + 1):
            var = (i / x) * 100
            self.bar["value"] = var
            sym = next(spin)
            self.precent.set(f"{int(var)}% {sym}")
            time.sleep(0.1)
            self.window.update_idletasks()
        self.download_status = True  # Устанавливаем True - программа выполнена
        time.sleep(5)
        self.window.destroy()

    # Метод для старта программы. Возвращает флаг
    def start(self):
        self.window.mainloop()
        return self.download_status
