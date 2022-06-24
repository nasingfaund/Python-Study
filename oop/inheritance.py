class Car:
    def __init__(self, year):
        self.name = "corolla"
        self.__make = "toyota"
        self._year = year

    def getYear(self):
        return self._year


class Car2(Car):
    def getYear(self):
        # обращение к полям через super() не работает
        # _ = protected
        print(self._year + 30)


car = Car2(1999)
car.getYear()

# будет ошибка, т.к. __ это private
# print(car.__make)
# но на самом деле доступ к private членам можно получить так:
print(car._Car__make)