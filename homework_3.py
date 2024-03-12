# # Завдання 1
word = input("Введіть слово: ")
reversed_word = word[::-1]

if word == reversed_word:
    print("+")
else:
    print("-")

# Завдання 2
text = input("Введіть текст: ")
word = input("Введіть слово, яке потрібно знайти: ")

if word in text:
    print("YES")
else:
    print("NO")

# # Завдання 3
mail = input("Введіть свою пошту: ")
if "@" and "." in mail:
    print("YES")
else:
    print("NO")

# Завдання 4
list = input("Введіть текст: ").strip().split()
list_len = len(list)
if list_len < 3:
    print("Кількість елементів менша за 3")
    print(list_len)
else: print(list[-3:])