# Написать функцию которая принимает целое число - number. Функция должна возвращать 'yes' если number является степенью двойки, иначе 'no'. Запрещено пользоваться функцией или оператором возведение в степень.
# Пример:
# is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256
# is_power_of_two(125) # 'no' потому что это не степень двойки

def is_power_of_two(number: int):
    if number == 1:
        return 'Yes'
    elif number < 1:
        return 'No'
    return is_power_of_two(number / 2)


print(is_power_of_two(16))
