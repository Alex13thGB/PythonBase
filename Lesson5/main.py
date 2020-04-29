"""
Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. Вызовите каждую функцию в main.py и проверьте что все работает как надо.

    Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.
"""

from task1 import make_dirs, remove_dirs
from task2 import get_element

make_dirs()
remove_dirs()

print(get_element([1, 2, 3, 4]))