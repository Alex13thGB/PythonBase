# Практическое задание 4
1. Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
3. Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
    * name - строка полученная от пользователя,
    * health = 100,
    * damage = 50. 
    * Поэкспериментируйте с значениями урона и жизней по желанию. 
    * Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои. 
    * Функция в качестве аргумента будет принимать атакующего и атакуемого. 
    * В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
    * Функция должна сама работать со словарями и изменять их значения.
4. Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
    * Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
    * Следовательно, у вас должно быть 2 функции:
    * Наносит урон. Это улучшенная версия функции из задачи 3.
    * Вычисляет урон по отношению к броне.

Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа. 
