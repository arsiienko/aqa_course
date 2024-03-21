# 1 Завдання

def sum_range(start: int, end: int):
    if start > end:
        start, end = end, start
    total = sum(range(start, end + 1))
    return total

# 2 Завдання

import math

def square(side):
    perimeter = side * 4
    area = side * side
    diagonal = side * math.sqrt(2)
    return perimeter, area, diagonal

print(square(5))

# 3 Завдання

def user_input():
    user_input_start = input('Введіть дані: ')
    return eval(user_input_start)

def type_of_input(data):
    try:
        if isinstance(data, dict):
            data_type = 'dict'
        elif isinstance(data, int):
            data_type = 'int'
        elif isinstance(data, list):
            data_type = 'list'
        elif isinstance(data, tuple):
            data_type = 'tuple'
        else:
            raise TypeError('Невідомий тип даних')
        print(f'User is going to work with {data_type}')
    except Exception as e:
        print(f'Виникла помилка: {e}')


data_type_operation = type_of_input(user_input())