"""
Создайте функцию, принимающую на вход имя, возраст и город проживания человека. 
Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
"""

def person_description(name, age, city):
    return f"{name}, {age} год(а), проживает в городе {city}"

print(person_description("Василий", 21, "Москва"))