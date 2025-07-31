from tkinter import messagebox


def get_space(entry_text: str, openings: list) -> None:  # type: ignore
    """Функция берет данные по проемам или перемычкам у пользователя"""

    pairs = entry_text.strip().split("),")  # Убираем пробелы и возвращаем список
    # Пример: "(1.0,2.4),(4.3, 5.8)" -> pairs = ["1.0,2.4", "(4.3, 5.8)"]
    for pair in pairs:  # pair = "(1.0,2.4", | pair = "(4.3, 5.8)"
        pair = (
            pair.replace("(", "").replace(")", "").strip()
        )  # pair = "1.0,2.4" | pair = "4.3, 5.8"
        if not pair:
            continue
        try:
            o_width, o_height = map(
                float, pair.split(",")
            )  # o_width = 1.0, o_height= 2.4 | o_width = 4.3, o_height = 5.8
            openings.append((o_width, o_height))  # type: ignore
        except ValueError:
            messagebox.showerror(
                title="Error",
                message=f"Неверный формат данных: {pair}. Должно быть (x, y)",
            )
            break


def save_in_file(data: str, /) -> None:
    """Функция сохраняет в файл .txt"""
    with open("save.txt", "a", encoding="UTF-8") as f:
        f.write("\n" + data + "\n")
