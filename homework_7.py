# Завдання 1
def map_custom(func, iterable):
    result = []
    for i in iterable:
        result.append(func(i))
    return result

def filter_custom(func, iterable):
    result = []
    for i in iterable:
        if func(i):
            result.append(i)
    return result

# Завдання 2
def function_x(x: int):
    return lambda y: y ** x

x = function_x(2)
print(x(3))

# Завдання 3
def console():
    function_name = input("Введіть назву функції: ")
    try:
        function_to_call = eval(function_name)
        argument = int(input("Введіть значення аргументу: "))
        print(function_to_call(argument))
    except NameError:
        print("Такої функції не існує")

console()