# 1 Завдання
l = str(["john", "marta", "james", "amanda", "marianna"]).title()
print(l)

# 2 Завдання
list1 = ["FirstItem", "FriendsList", "MyTuple"]
list2 = []

for variable in list1:
    snake_case = ''.join(['_' + c.lower() if c.isupper() else c for c in variable]).lstrip('_')
    list2.append(snake_case)

print(list2)


# 3 Завдання
d = {'language': 'C++', 'developer': 'Bjarne Stroustrup', 'language1': 'Python', 'developer1': 'Guido van Rossum',
     'language2': 'Java', 'developer2': 'James Gosling', 'language3': 'Javascript','developer3': 'Brendan Eich'}
print(f'My favorite programming language is {d['language']}. It was created by {d['developer']}')
print(f'My favorite programming language is {d['language1']}. It was created by {d['developer1']}')
print(f'My favorite programming language is {d['language2']}. It was created by {d['developer2']}')
print(f'My favorite programming language is {d['language3']}. It was created by {d['developer3']}')

del d['language']
del d['developer']
print(d)

# 4 Завдання
names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
for name in names:
    if not isinstance(name, str):
        continue
    print(name)

# 5 Завдання
types = [1, 1000, 2, 12, {'key': 'value'}]

for item in types:
    if isinstance(item, int):
        print(item)
    else:
        print(f'Цикл не працює з {type(item)} типом даних')
        break

# 6 Завдання
input_string = input('Введіть рядок: ')
char_count = {}
for char in input_string:
    char_count[char] = char_count.get(char, 0) + 1
result = ', '.join([f'{char},{count}' for char, count in char_count.items()])
print(result)
