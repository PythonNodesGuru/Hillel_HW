# Написать класс Timer для измерения времени выполнения кода.
# Прошедшее время должен возвращать в аттрибуте elapsed_time.
# Класс должен применяться как контекстный менеджер.
# У класса должен быть метод reset.
# Если между использованием контекстного менеджера вызывался метод reset, прошедшее время должно считаться заново.
# Если метод reset не вызывался, в elapsed_time должно быть сохранено время выполнения всех фрагментов кода обернутых контекстным менеджером.
import time


class Timer:

    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.end = time.time()

    @property
    def elapsed_time(self):
        delta = time.time() - self.start
        return delta

    def reset(self):
        self.start = time.time()


# Пример использования:
with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 second
with t:
    time.sleep(2)
print(t.elapsed_time)  # ~3 seconds

with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 seconds