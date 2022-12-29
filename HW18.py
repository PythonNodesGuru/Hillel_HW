# Написать класс-миксин, наследуя который объект будет выводится в консоль в виде имени класса и словаря аттрибутов со значениями:
# ClassName: {
#     key: value
# }


class AttributePrinterMixin:
    def __str__(self):
        class_name = self.__class__.__name__
        rows = []

        for k, v in self.__dict__.items():
            if k.startswith(f'_{class_name}__'):
                k = k.replace(f'_{class_name}__', '')
            if k.startswith('_'):
                k = k[1:]
            rows.append(f'{k}: {v}')

        output_value = ''

        for row in rows:
            output_value+=f'\n    {row}'
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