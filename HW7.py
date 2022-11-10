# Задание 1
# Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers
#
# Задание 2
# Запросить у пользователя текст и записать его в файл data.txt
#
# Задание 3
# Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел
#
# Задание 4
# Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
#
# Задание 5
# Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
#
# Задание 6
# Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел
#
# Задание 7
# Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
#
# 'в' - 20 раз
# 'привет' - 10 раз
# 'как' - 9 раз
# 'у' - 7
# 'world' - 4
import collections
import random

# Task1
f = open('data.txt', 'r')
data = f.read().split()
new_list = []
n = ''
for i in data:
    if i.isdigit():
        new_list.append(int(i))
    elif i.isalpha():
        continue
    else:
        for char in i:
            if char.isdigit():
                n += char
        new_list.append(int(n))
        n = ''
print(new_list)
f.close()

# Task2
text = input('Enter your text: ')
f = open('data.txt', 'w')
f.write(text)
f.close()

# Task3
quantity_number = int(input('Enter quantity of numbers: '))
f = open('number.txt', 'w')
for _ in range(quantity_number):
    number = str(input('Enter number: '))
    f.write(number + ' ')
f.close()

# Task4
random_numbers = [random.randint(1,10) for _ in range(100)]
f = open('number.txt', 'w')
for i in random_numbers:
    f.write(str(i) + '\n')
f.close()

# Task5
f = open('data.txt', 'r')
data = f.readlines()
words_count = 0
for line in data:
    words_count += len(line.split())
print(f'Number of words: {words_count}')
f.close()

# Task6
f = open('number.txt', 'r')
data = f.read().split()
sum = 0
for lines in data:
    sum +=int(lines)
print(f'Sum of numbers: {sum}')
f.close()

# Task7
f = open('file.txt', 'r')
data = f.read().split()
counter = collections.Counter(data).most_common(5)
j = 0
k = 0
for i in counter:
    key = counter[j][k]
    k += 1
    value = counter[j][k]
    print(f' {key} - {value} times')
    j += 1
    k = 0
print(counter)
f.close()


