# Task1
# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.
# Task2
# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением. Предполагается,
# что элементы списка будут соответствовать правилам задания ключей в словарях.
# Task3
# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
# Task4
# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и
# выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).

# Task1
def change(user_list):
    if len(user_list) == 0:
        for i in range(2):
            print('Лист должен содеражть мин. 2 элемента, введите ваше значение:')
            user_list.append(input())
        print(user_list)
        user_list[0], user_list[- 1] = user_list[- 1], user_list[0]
        return list
    elif len(user_list) < 2:
        print('Лист должен содеражть мин. 2 элемента, введите ваше значение:')
        user_list.append(input())
        print(user_list)
        user_list[0], user_list[- 1] = user_list[- 1], user_list[0]
        return user_list
    else:
        user_list[0], user_list[- 1] = user_list[- 1], user_list[0]
        return user_list


# Task2
def to_dict(lst):
    lst_dictionary = {str(key): key for key in lst}
    print(lst_dictionary)
    return lst_dictionary


# Task3
def sum_range(start, end):
    if start < end:
        sum_num = 0
        for i in range(start, end + 1):
            sum_num += i
        return sum_num
    elif start > end:
        sum_num = 0
        for i in range(end, start + 1):
            sum_num += i
        return sum_num
    else:
        print(f'start value {start} and end value {end} are equal')
        return 0


# Task4
def read_last(lines, file):
    if lines > 0:
        f = open(file, 'r')
        data = f.readlines()[-lines:]
        for line in data:
            print(line)
    else:
        print(f'Lines should be positive number or more then zero ')
