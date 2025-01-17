"""
Напишите функцию которая принимает на вход список.
* Функция создает из этого списка новый список из квадратных корней чисел
  (если число положительное) и самих чисел (если число отрицательное)
  и возвращает результат (желательно применить генератор и тернарный оператор
  при необходимости).
* В результате работы функции исходный список не должен измениться.

    Например:
    old_list = [1, -3, 4]
    result = [1, -3, 2]
"""
import math, random


def convert_list(numbers):
    return [number if number < 0 else round(math.sqrt(number), 2)  for number in numbers]


old_list = [random.randint(-100, 100) for i in range(20)]

print(f"Generated list: {convert_list(old_list)}")
print(f"Source list: {old_list}")
