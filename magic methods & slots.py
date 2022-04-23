class Car:

    def __init__(self, vendor, model, max_speed):
        self.__vendor = vendor
        self.__model = model
        self.__max_speed = max_speed

    # __repr__ должен возвращать строку, показывающую, как может быть создан экземпляр
    # (формальное строковое представление объекта)
    def __repr__(self):
        return f'Car({self.__vendor!r}, {self.__model!r}, {self.__max_speed!r})'

    # предназначен для чтения людьми. вызывается как print(<object>)
    def __str__(self):
        return f'vendor: {self.__vendor}, model: {self.__model}'


car = Car('Toyota', 'Supra', 250)
# сработает __str__, т.к. его переопределили
print(car)

# выводит список доступных членов объекта
print(car.__dir__())

car2 = eval(repr(car))
print(type(car2))
print(car2)


class SlotsClass:
    __slots__ = ('foo', 'bar')

    def __init__(self, foo_value):
        self.foo = foo_value


class ChildSlotsClass(SlotsClass):

    def __init__(self, foo_value):
        __slots__ = ('baz')
        super(ChildSlotsClass, self).__init__(foo_value)


slots_obj = ChildSlotsClass('foo_value')
slots_obj.baz = 2

# дочерний класс видит слоты родителя и свои слоты
print(slots_obj.baz, slots_obj.foo)

# нужно закомментить создание слотов в ChildSlotsClass, чтобы получить __dict__
# __dict__ не создается, если создаются слоты
print(slots_obj.__dict__)