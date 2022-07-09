class Vector:
    min_coord = 5
    max_coord = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # метода КЛАССА. может менять только поля класса, но не экземпляра
    # cls не знает об x и y - полях инстанса класса
    @classmethod
    def is_coord_hit(cls, coord):
        return cls.min_coord <= coord <= cls.max_coord

    @staticmethod
    def get_norm(x, y):
        return x ** 2 + y ** 2

    # метода ЭКЗЕМПЛЯРА класса
    def get_coord(self):
        return self.x, self.y


# classmethod вызывается из класса
# также его можно вызвать через инстанс. инстанс имеет доступ к своим полям и к полям класса
print(Vector.is_coord_hit(5))
# staticmethod это обычный статический метод. он не имеет доступ к полям класса, по сути это обычный метод
print(Vector.get_norm(5, 6))
