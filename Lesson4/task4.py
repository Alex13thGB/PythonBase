"""
Пара сущностей player и enemy через словарь, который будет иметь
ключи и значения:
    name - строка полученная от пользователя,
    health = 100,
    damage = 50.

Давайте усложним предыдущее задание. Измените сущности,
    добавив новый параметр - armor = 1.2 (величина брони персонажа)
    Теперь надо добавить новую функцию, которая будет вычислять и
    возвращать полученный урон по формуле damage / armor
    Следовательно, у вас должно быть 2 функции:
    Наносит урон. Это улучшенная версия функции из задачи 3.
    Вычисляет урон по отношению к броне.
"""


def get_damage(damage, armor):
    return round(damage / armor, 2)


def attack(person1, person2):
    person2["health"] -= get_damage(person1["damage"], person2["armor"])


player = {"name": "Player", "health": 100, "damage": 20, "armor": 1.2}
enemy = {"name": "Enemy", "health": 100, "damage": 30, "armor": 1.2}

print(player)
print(enemy)

attack(player, enemy)
print(player)
print(enemy)

attack(enemy, player)
print(player)
print(enemy)
