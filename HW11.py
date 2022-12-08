# Написать функцию, которая возвращает слуайную строку заданной длины.
# Строка должна состоять из больших и маленьких латинских букв и цифр.

import random

upper_letters = [i for i in range(65, 91)]
lover_letters = [i for i in range(97, 123)]
digits_letters = [i for i in range(48, 58)]


def get_random_string(length: int) -> str:
    new_rnd_str = ""
    for i in range(length):
        c = chr(random.choice(upper_letters + lover_letters + digits_letters))
        new_rnd_str += c
    return new_rnd_str


print(get_random_string(100))
