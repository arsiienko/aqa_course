# 1 Завдання

class NumberError(Exception):
    pass

try:
    number = int(input("Введіть число: "))
    if number < 0:
        raise NumberError("Корінь від'ємного числа не існує")
    square_root = number ** 0.5
except NumberError as n:
    print(n)
else:
    print("Квадратний корінь числа:", square_root)
finally:
    print("Операція обчислення завершена")


# 2 Завдання
try:
    number = float(input("Введіть число: "))
    if number < 0:
        raise NumberError("Корінь від'ємного числа не існує")
    square_root = number ** 0.5
except ValueError:
    print("Будь ласка, введіть коректне число")
except NumberError as n:
    print(n)
else:
    print("Квадратний корінь числа:", square_root)
finally:
    print("Операція обчислення завершена")

# 3 Завдання

while True:
    try:
        num1 = input("Введіть перше число або 'вихід' щоб вийти: ")
        if num1.lower() == 'вихід':
            break
        num1 = int(num1)
        num2 = int(input('Введіть друге число: '))
        operation = input('Введіть арифметичну операцію (+, -, *, /): ')

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print('Ділення на нуль неможливе')
                continue
        else:
            print('Невірна операція')
            continue
        print('Результат:', result)
    except ValueError:
        print('Будь ласка, введіть коректне число')
    except ZeroDivisionError:
        print('Ділення на нуль неможливе')
    except Exception as e:
        print(f'Виникла помилка: {e}')
    finally:
        print('Операція обчислення завершена')



