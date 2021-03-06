"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
import hashlib

word = input('Введите строку состоящую только из строчных латинских букв - ')

res = set()

for i in range(len(word)):
    for j in range(len(word), i, -1):
        hash_str = hashlib.sha256(word[i:j].encode('utf-8')).hexdigest()
        res.add(hash_str)

print(f'{len(res) -1} различных подстрок в строке {word}.')