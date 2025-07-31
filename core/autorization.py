from tkinter import *  # type: ignore
from tkinter.font import BOLD  # type: ignore


class Autorization:
    # Создаем окно
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Login form")
        self.window.geometry("440x440")
        self.window.resizable(False, False)
        self.window.configure(bg="#010101")
        icon = PhotoImage(file="icons/fox_icon.png")
        self.window.iconphoto(True, icon)

        self.success = (
            False  # Флаг, чтобы следующая программа запускалась после авторизации
        )
        # Основной фрейм, который поместим в центр
        self.frame = Frame(self.window, bg="#010101")
        # Статус, который будет оповещать об успешном входе или не успешном входе
        self.status = StringVar()
        self.label_status = Label(
            self.frame,
            textvariable=self.status,
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        # Главный лейбл
        self.label = Label(
            self.frame,
            text="Авторизация",
            bg="#010101",
            fg="#750000",
            font=("Ink Free", 36, BOLD),
        )
        # Лейбл с имя пользователя
        self.label_username = Label(
            self.frame, text="Логин:", bg="#010101", fg="#FFFFFF", font=("Ink Free", 16)
        )
        # Лейбл пароля
        self.label_password = Label(
            self.frame,
            text="Пароль:",
            bg="#010101",
            fg="#FFFFFF",
            font=("Ink Free", 16),
        )
        # Даём пользователю ввести логин и пароль
        self.entry_username = Entry(self.frame, font=("Arial", 16))
        self.entry_password = Entry(self.frame, show="*", font=("Ink Free", 16))
        # Кнопка для входа
        self.button = Button(
            self.frame,
            text="Войти",
            bg="#750000",
            fg="#FFFFFF",
            font=("Ink Free", 16),
            command=self.__login,
        )
        # Создаем сетку из всех виджетов
        self.label.grid(row=0, column=0, columnspan=2, sticky="news", pady=16)
        self.label_username.grid(row=1, column=0, padx=16)
        self.label_password.grid(row=2, column=0)
        self.entry_username.grid(row=1, column=1, pady=20)
        self.entry_password.grid(row=2, column=1, pady=20)
        self.button.grid(row=4, column=0, columnspan=2, pady=10)
        # Отдельно статус
        self.label_status.grid(row=3, column=0, columnspan=2)
        # Распаковываем фрейм, и устанавливаем его в центр
        self.frame.pack(expand=True)

    # Этот метод уничтожает окно после успешного ввода логина и пароля (можно вынести - логика)
    def __crush(self):
        self.success = (
            True  # Тут меняем флаг на True - где программа уже почти "закрывается"
        )
        self.window.after(5000, self.window.destroy)

    # Метод, который проверяет логин и пароль (можно вынести -логика)
    def __login(self):
        username = "Admin"
        password = "admin1234"
        if (
            self.entry_username.get() == username
            and self.entry_password.get() == password
        ):
            self.status.set("Вы вошли в систему!\nВход..")
            self.window.after(2000, self.__crush)

        else:
            self.status.set("Неверный логин или пароль")

    # Метод для старта утилиты. Возвращает флаг, при успешном вводе.
    def start(self):
        self.window.mainloop()
        return self.success
