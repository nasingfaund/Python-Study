class Numbers:

    def __init__(self):
        self.__list = []

    def append(self, value):
        self.__list.append(value)

    def append(self, *values):
        for value in values:
            self.__list.append(value)

    def print(self):
        for v in self.__list:
            print(v, end=' ')

    # реализуем getitem, чтобы обращаться к объекту класса как к списку
    def __getitem__(self, index):
        return self.__list[index]


numbers = Numbers()
numbers.append(3, 5, 6, 2)
numbers.print()
# теперь можно обращаться к элементам списка напрямую через объект!
print('indexator test: ', numbers[2])

# также теперь можно преобразовать инстанс класса в список, т.к.
# мы реализовали __getitem__ - один из методов протокола iterable
print(type(numbers))
numbers = list(numbers)
print(numbers, type(numbers))


