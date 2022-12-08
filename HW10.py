# Написать декоратор call_times, который будет принимать в качестве
# параметра file_name, считать количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'


from collections import defaultdict

counts = defaultdict(int)
file_dict = defaultdict(dict)


def call_times(file_name):
    def inner(func):
        def wrapper():
            counts[func] += 1
            file_dict[file_name][func] = counts[func]
            f = open(file_name, 'w')
            for key, value in file_dict[file_name].items():
                if value > 0:
                    f.write(f'{key.__name__} была вызвана {value} раза.\n')
            return func()
        return wrapper
    return inner


@call_times('foo.txt')
def foo():
    pass


@call_times('foo.txt')
def boo():
    pass


@call_times('calls.txt')
def doo():
    pass


foo()
foo()
doo()
boo()
foo()
boo()
doo()

