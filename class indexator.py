class Numbers:

    def __init__(self):
        self.__list = []

    def append(self, *values):
        for value in values:
            self.__list.append(value)

    # реализуем getitem, чтобы обращаться к объекту класса как к списку
    def __getitem__(self, index):
        return self.__list[index]


numbers = Numbers()
numbers.append(3, 5, 6, 2)
# теперь можно обращаться к элементам списка напрямую через объект!
print(f'2-ой элемент в списке: {numbers[2]}')

# также теперь можно преобразовать инстанс класса в список, т.к.
# мы реализовали __getitem__ - один из методов протокола iterable
numbers = list(numbers)
print(numbers, type(numbers))


