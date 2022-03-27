from datetime import date


class Person:

    # private поле класса (не объекта)
    # такое поле является общим для всех объектов класса
    __persons_count = 0
    class_description = 'person entity'

    def __init__(self, name, age):
        # через self обратиться не удастся, т.к. это поле является членом КЛАССА, а self - это объект класса
        self.__age = age
        # переменная объекта класса
        self.__name = name
        Person.__persons_count += 1

    # можно вызвать и только через обращение к классу
    # пример использования: функция в контексте сущности. так мы не засоряем общее пространство имен
    @staticmethod
    def is_adult(age):
        return True if age >= 18 else False

    # можно вызвать и через объект и через класс
    # пример использования: фабричный метод (альтернативный конструктор класса)
    @classmethod
    def createFromBirthYear(cls, name, birthYear):
        age = date.today().year - birthYear
        return cls(name, age)

    def getinfo(self):
        return f'{self.Name} is {self.Age}'

    # переопределяем метод __str__, чтобы иметь возможность отображать
    # информацию об объекте с помощью print(person)
    def __str__(self):
        return self.getinfo()

    @classmethod
    def getPersonsCount(cls):
        return cls.__persons_count

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, newName):
        self.__name = newName

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, newAge):
        self.__age = newAge

    def _protected_method(self):
        print('protected method')

    def __private_method(self):
        print('private method')


class Person2(Person):

    def __init__(self):
        pass

    pass

person = Person.createFromBirthYear('Eva', 2007)
print(Person.is_adult(person.Age))

# так можно делать за счет переопределения метода __str__
print(person)

print(f'personsCount: {Person.getPersonsCount()}')

# свойства
print(person.Name)
print(person.Age)

# private/protected методы
# IDE сругается
#person.__private_method(
Person2()._protected_method()

# на самом деле в пайтоне нет поддержки модификаторов доступа
# _ и __ это всего лишь общепринятые понятия
# ниже мы можем получить доступ к типа скрытому полю класса через его инстанс:
print(person._Person__age)

# различия между classmethod и staticmethod:
# 1. staticmethod не имеет ссылку ни на объект класса (self), ни на сам класс (cls)
# следовательно с помощью такого метода мы не сможем обратиться к членам класса
# staticmethod это точно то же самое, что и обычный метод, только в контексте класса

# 2. classmethod имеет ссылку на класс - cls. она позволяет обращаться к членам класса
# можно использовать как фабричный метод (альтернативный конструктор класса)
