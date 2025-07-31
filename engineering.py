from core.interface import Interface
from core.autorization import Autorization
from core.progress import Progress


def main():
    try:
        progress = Progress()
        dowload_success = progress.start()

        if dowload_success:
            autorization = Autorization()
            success = autorization.start()
        else:
            print("Авторизация не пройдена!")
        if success:  # type: ignore
            window = Interface()
            window.start()
    except UnboundLocalError:
        print("Программа дала сбой!")


if __name__ == "__main__":
    main()
