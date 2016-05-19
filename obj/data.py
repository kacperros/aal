class Data:
    def __init__(self):
        self.data_sets = []

    def get_data_set(self, position):
        return self.data_sets[position]

    def append(self, data_set):
        self.data_sets.append(data_set)

    def get_data_sets(self):
        return self.data_sets
