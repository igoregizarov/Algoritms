"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

base_list = [1, -0.5, 0.25, -0.125]

n_elem = int(input('Введите количество элементов: '))


def sum_elem(n):
    if n == 1:
        return base_list[n - 1]
    else:
        return base_list[n - 1] + sum_elem(n - 1)


print(f'Количество элементов - {n_elem}, их сумма - {sum_elem(n_elem)}')