from Encapsulation import Book


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch


novel1 = Novel('Novel Book', 20, 'Novel Author', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python', 12, 'Python Author', 655, 'IT')

print(novel1)
print(academic1)
