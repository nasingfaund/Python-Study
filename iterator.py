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

#for value in iterator:
    #print(value)


# будет выход за границы итератора
# for i in range(1, 7):
#     print(next(iterator))

# 2. Неявная реализация
def increase(count):
    value = currentCount = 0
    while currentCount < count:
        value += 2
        currentCount += 1
        yield value


generator = increase(5)
for i in generator:
    print(i)