"""
Создать модуль *music_serialize.py*.
    В этом модуле определить словарь для вашей любимой музыкальной группы,
    например:
        my_favourite_group = {
        ‘name’: ‘Г.М.О.’,
        ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
        ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
        {‘name’: ‘Шапито’,‘year’: 2014}]}

    С помощью модулей json и pickle сериализовать данный словарь в json
    и в байты, вывести результаты в терминал.
    Записать результаты в файлы group.json, group.pickle соответственно.
    В файле group.json указать кодировку utf-8.
"""

import json
import pickle

my_favourite_group = {
    "name": "Г.М.О.",
    "tracks": ["Последний месяц осени", "Шапито"],
    "Albums": [{"name": "Делать панк-рок", "year": 2016},
               {"name": "Шапито", "year": 2014}]}

my_fav_group_json = json.dumps(my_favourite_group)
print("JSON:", my_fav_group_json)

my_fav_group_pickle = pickle.dumps(my_favourite_group)
print("PICKLE:", my_fav_group_pickle)

with open("group.json", "w", encoding="utf-8") as f_json:
    json.dump(my_favourite_group, f_json)

with open("group.pickle", "wb") as f_pickle:
    pickle.dump(my_favourite_group, f_pickle)
