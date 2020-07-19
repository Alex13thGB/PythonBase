"""
Создать модуль music_deserialize.py.
    * В этом модуле открыть файлы group.json и group.pickle,
      прочитать из них информацию.
    * И получить объект: словарь из предыдущего задания.
"""

import json
import pickle

with open("group.json", "r", encoding="utf-8") as f_json:
    group_json = json.load(f_json)
print("JSON:", group_json)

with open("group.pickle", "rb") as f_pickle:
    group_pickle = pickle.load(f_pickle)
print("PICLE:", group_pickle)
