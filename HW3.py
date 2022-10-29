# HW3
# Пользователь вводит с клавиатуры три числа в переменные a, b, c. Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no
# Пользователь вводит с клавиатуры три числа в переменные a, b, c. Найдите наибольшее число из них и запишите в переменную max.
# Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.


a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
c = int(input('Enter number C: '))

# Task1
if a > 10 and b > 10 and c > 10:
    if a % 3 == 0 and b % 3 == 0:
        print('yes')
    else:
        print('no')

# Task2
max_num = a
if max_num < b:
    max_num = b
if max_num < c:
    max_num = c
print(f'max number: {max_num}')

# Task3 (while)
sum_odd = 0
while a >= b:
    print('The value of A cannot be greater than the value of B')
    a = int(input('Enter number A: '))
    b = int(input('Enter number B: '))

while a <= b:
    if a % 2 == 0:
        print(a)
        sum_odd += a
    a += 1
print(f'The sum of odd numbers =  {sum_odd} ')

# Task3 (for)

for i in range(a, b):
    if i % 2 == 0:
        print(i)
        sum_odd += i
print(f'The sum of odd numbers =  {sum_odd} ')
