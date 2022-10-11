# 1. явная реализация протокола итератора
class IteratorClass:
    def __init__(self):
        self.collection = [x for x in range(2, 11) if x % 2 == 0]
        self.current_index = -1

    def __iter__(self):
        return self

    def get_current_value(self):
        return self.collection[self.current_index]

    def __next__(self):
        self.current_index += 1

        if self.current_index < len(self.collection):
            return self.get_current_value()
        else:
            raise StopIteration


iterator = IteratorClass()

for v in iterator:
    print(v, end=' ')

print()

# 2. каст объекта к итератору
it = iter([v for v in range(2, 11) if v % 2 == 0])

for v in it:
    print(v, end=' ')
