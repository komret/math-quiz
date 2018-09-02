class Player:
    def __init__(self, order, name):
        self.order = order
        self.name = name
        self.add_times = []
        self.subtract_times = []
        self.multiply_times = []
        self.divide_times = []

    def __str__(self):
        return self.name

    def __et__(self, other):
        return self.count_times() == other.count_times()

    def __lt__(self, other):
        return self.count_times() < other.count_times()

    def count_times(self):
        return sum(self.add_times) + sum(self.subtract_times) + sum(self.multiply_times) + sum(self.divide_times)
