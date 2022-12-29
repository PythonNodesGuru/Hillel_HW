# Написать класс-миксин, наследуя который объект будет выводится в консоль в виде имени класса и словаря аттрибутов со значениями:
# ClassName: {
#     key: value
# }


class AttributePrinterMixin:
    def __str__(self):
        class_name = self.__class__.__name__
        rows = []

        for k, v in self.__dict__.items():
            for parent in self.__class__.__bases__:
                parent_name = parent.__name__
                if k.startswith(f'_{parent_name}__'):
                    k = k.replace(f'_{parent_name}__', '')
            if k.startswith(f'_{class_name}__'):
                k = k.replace(f'_{class_name}__', '')
            if k.startswith('_'):
                k = k[1:]
            rows.append(f'{k}: {v}')

        output_value = ''

        for row in rows:
            output_value += f'\n    {row}'
        return f'''{class_name}: {{{output_value}\n}}'''

# Протектед и приватные аттрибуты должны выводить только свое имя (без знака подчеркивания для протектед и префикса "_<имя класса>__")
# Каждя строка с полем начинается с символа табуляции.
# Если класс наслудует другие классы, их аттрибуты тоже должны выводится по тем же правилам.
# Свойства обрабатывать не надо.

# Пример:
class A(AttributePrinterMixin):
    def __init__(self):
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]
a = A()
print(a)
# A: {
#    public_filed: 3
#    protected_field: q
#    private_field: [1, 2, 3]
# }


# Можно сказать, что дальше это уже задача со звездочкой, но у тебя не процессятся приватные аттрибуты суперклассов
class Super:
    def __init__(self):
        self.__super_private = 111

class Sub(Super, AttributePrinterMixin):
    def __init__(self):
        super().__init__()

sub = Sub()
print(sub)

"""
Sub: {
    Super__super_private: 111  # Should be super_private: 111
}
"""