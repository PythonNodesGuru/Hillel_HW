# Задание 1:
# Запросить у пользователя 5 чисел и записать их в список
#
# Задание 2:
# Дан список A = [1, 2, 3, 4, 5]
# Удалить последнее число из списка

# Задание 3:
# Запросить у пользователя 10 чисел и записать их в список A
# Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N
#
# Задание 4:
# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности
#
# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C
#
# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.
#
# Задание 7:
# Пользователь вводит текст нужно вывести количество чисел в этом тексте
# Пример:
# > 'Lorem 222 ipsum, 123 dolor 1 sit amet
# Количество чисел: 3

# Task1
new_list = []
for _ in range(5):
    number = int(input('Enter number: '))
    new_list.append(number)
print(new_list)

# Task2
new_list = [1, 2, 3, 4, 5]
last_number = int(new_list[int((len(new_list)) - 1)])
new_list.remove(last_number)
print(new_list)

# Task3
new_list = []
for _ in range(10):
    number = int(input('Enter number: '))
    new_list.append(number)
print(new_list)
search_number = int(input('Enter your search number: '))
print(f'Your number repeat {new_list.count(search_number)} time')

# Task4
quantity_number = int(input('Enter quantity of numbers: '))
new_list = []
for _ in range(quantity_number):
    number = int(input('Enter number: '))
    new_list.append(number)
print(f'Your direct list: {new_list}')
new_list.reverse()
print(f'Your reverse list: {new_list}')

# Task5
new_list_a = []
new_list_b = []
for i in range(5):
    number = int(input('Enter number: '))
    new_list_a.append(number)
    if int(new_list_a[i]) > 5:
        new_list_b.append(new_list_a[i])
print(new_list_a)
print(new_list_b)

# Task6
new_list = []
quantity_number = int(input('Enter quantity of numbers: '))
for _ in range(quantity_number):
    number = int(input('Enter number: '))
    new_list.append(number)
max_number = new_list[0]
min_number = new_list[0]
for j in range(quantity_number):
    if new_list[j] < min_number:
        min_number = new_list[j]
    elif new_list[j] > max_number:
        max_number = new_list[j]

print(new_list)
print(f'Your max number: {max_number}')
print(f'Your min number: {min_number}')

# Task7

text = input('Enter text:').split()
digit_counter = 0
for i in text:
    if i.isdigit():
        digit_counter += 1
if digit_counter == 0:
    print('The text does not have numbers')
else:
    print(f'Count of numbers: {digit_counter}')

