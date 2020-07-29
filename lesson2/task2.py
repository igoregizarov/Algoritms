"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
number = input('Введите число: ')
n_len = len(number)
n_chet = 0
n_ne_chet = 0


def check():
    global n_len, n_chet, n_ne_chet
    if n_len == 0:
        return print(f'Количество четных и нечетных цифр в числе равно: ({n_chet}, {n_ne_chet})')
    else:
        if int(number[n_len - 1]) % 2 == 0:
            n_chet += 1
        else:
            n_ne_chet += 1
    n_len -= 1
    check()


check()
