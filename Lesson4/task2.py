"""
    Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
"""

def max_number(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:
        return c

def get_max(a, b, c): # Правильное решение
    return max([a, b, c])

print(max_number(1, 2, 3))
print(max_number(2, 3, 1))
print(max_number(3, 2, 1))
print(max_number(3, 1, 2))