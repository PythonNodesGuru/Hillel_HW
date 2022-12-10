# Написать функцию, которая принимает несколько итерируемых объектов,
# и возвращает список из кортежей составленных из элементов итерируемых объектов одного индекса.
# Функция также должна принимать параметры с дефолтными значения:
# full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной
# default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default


from collections.abc import Iterable
from typing import List, Tuple


def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
    if full is False:
        length = min(map(len, sequences))
        result = []
        print(sequences[0])
        for index in range(length):
            new_item = tuple(map(lambda item: item[index], sequences))
            result.append(new_item)
        return result
    else:
        length = max(map(len, sequences))
        result = []
        for index in range(length):
            new_item = tuple(map(lambda item: item[index] if len(item) > index else default, sequences))
            result.append(new_item)
        return result


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
seq3 = [91, 18]

print(custom_zip(seq1, seq2, seq3))
print(custom_zip(seq1, seq2,seq3, full=True, default="Q"))

