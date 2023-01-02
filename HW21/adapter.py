from adaptee import EuroFork


class AdapterEuroInUsa:

    def __init__(self):
        self._euro_fork = EuroFork()

    def power_usa(self):
        self._euro_fork.power_euro()
