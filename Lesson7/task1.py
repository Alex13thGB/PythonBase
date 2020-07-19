"""
Даны два списка фруктов. Получить список фруктов, присутствующих
в обоих исходных списках.
 Примечание:
   Списки фруктов создайте вручную в начале файла.
"""

fruits1 = ["apple", "grape", "papaya", "mango", "lemon", "pear", "avocado"]
fruits2 = ["banana", "orange", "mango", "apple", "cherry", "grape", "lemon"]

fruits = [fruit for fruit in fruits1 if fruit in fruits2]

print(fruits)
