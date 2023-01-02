class UsaFork:
    def power_usa(self):
        print('power on. Usa')


# Американская розетка
class UsaSocket:
    def __init__(self, fork):
        self.fork = fork

    def connect(self):
        self.fork.power_usa()
