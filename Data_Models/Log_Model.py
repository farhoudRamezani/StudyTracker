class LogSystem:
    def __init__(self, data):
        self.data = data

    def add(self, subject):
        if subject.name in self.data:
            self.data[subject.name].update(subject.dates)
        else:
            self.data[subject.name] = subject.dates.copy()