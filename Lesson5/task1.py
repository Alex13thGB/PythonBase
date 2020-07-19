"""
Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
    * В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из
      которой запущен данный код.
    * Затем создайте вторую функцию удаляющую эти папки.
      Проверьте работу функцийв этом же модуле.
"""
import os


def make_dirs():
    for i in range(1, 10):
        dir_name = f"dir_{i}"
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)


def remove_dirs():
    for i in range(1, 10):
        dir_name = f"dir_{i}"
        if os.path.exists(dir_name):
            os.rmdir(dir_name)


if __name__ == "__main__":
    make_dirs()
    remove_dirs()
