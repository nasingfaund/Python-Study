from abc import ABC, abstractmethod


# абстрактный класс велосипеда. объект этого класса создать невозможно
class Bike(ABC):

    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    # абстрактный метод обязательно должен быть реализован наследниками
    @abstractmethod
    def move(self):
        print('default move')
        pass


class UsualBike(Bike):

    def __init__(self, model, bikeType, speed):
        super().__init__(model, speed)
        self.bikeType = bikeType

    def move(self):
        super().move()
        print(f'{self.bikeType} bike {self.model} move with speed {self.speed}')


class MountainBike(Bike):

    def __init__(self, model, bikeType, speed):
        super().__init__(model, speed)
        self.bikeType = bikeType

    def move(self):
        print(f'{self.bikeType} bike {self.model} move with speed {self.speed}')


bike = UsualBike('Forward', 'usual', 20)
bike.move()

bike = MountainBike('Stels', 'mountain', 50)
bike.move()
