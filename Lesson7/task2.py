"""
Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих следующим условиям:
    Элемент кратен 3,
    Элемент положительный,
    Элемент не кратен 4.
Примечание:
   Список с целыми числами создайте вручную в начале файла. 
   Не забудьте включить туда отрицательные числа.
   10-20 чисел в списке вполне достаточно.
"""
import random

numbers = [random.randint(-100, 100) for i in range(20)]
print("Source list:", numbers)

numbers = [number for number in numbers if number % 3 == 0 and number > 0 and number % 4 != 0]
print("Generated list:", numbers)