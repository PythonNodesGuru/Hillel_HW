# Запросить у пользователя число N - ширина треугольника.
#
#
# Вывести треугольник #1 с шириной N с помощью цикла while
# Вывести треугольник #2 с шириной N с помощью цикла while
# Задание со звездочкой:
#
# Вывести треугольник #3 с шириной N с помощью цикла while
# Вывести треугольник #4 с шириной N с помощью цикла while


width = int(input('Enter the width of the triangle: '))

while width > 0:
    print('*' * width)
    width -= 1

width = int(input('Enter the width of the triangle: '))
i = 0
j = width
while i < width:
    i += 1
    k = 0
    while j > k:
        k += 1
        print('*', end='')
    j -= 1
    print()


width = int(input('Enter the width of the triangle: '))
i = 1
while width >= i:
    print('*' * i)
    i += 1

width = int(input('Enter the width of the triangle: '))
i = 0
while i < width:
    i += 1
    j = 0
    while j < i:
        j += 1
        print('*', end='')
    print()


width = int(input('Enter the width of the triangle: '))
i = 0
while width > 0:
    print(' ' * i + '*' * width)
    width -= 1
    i += 1

width = int(input('Enter the width of the triangle: '))
i = 1
while width > 0:
    print(' ' * int(width - 1) + '*' * i)
    width -= 1
    i += 1




