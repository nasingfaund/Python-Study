# 1. Явная реализация
class IncreaseByTwo:
    def __init__(self, count):
        self.count = count
        self.currentValue = 0
        self.currentCount = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.currentCount < self.count:
            self.currentValue += 2
            self.currentCount += 1
            return self.currentValue
        else:
            raise StopIteration


iterator = IncreaseByTwo(5)

for v in iterator:
    print(v)


# итерируемый объект из списка
l = [v for v in range(2, 11) if v % 2 == 0]
it = iter(l)

for v in it:
    print(v)