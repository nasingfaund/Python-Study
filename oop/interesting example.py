class Base:
    def __init__(self):
        print('Base')
        pass

    def T(self):
        print('Base T')


class X(Base):
    def __init__(self):
        super().__init__()
        print('X')

    def T(self):
        print('X T')


class Y(Base):
    def __init__(self):
        super().__init__()
        print('Y')

    def T(self):
        print('Y T')


class Z(X, Y):
    def __init__(self):
        super().__init__()
        print('Z')

    def test(self):
        self.T()

# проверка того, что напечатается из конструкторов классов
z = Z()

# проверка того, какой именно метод T вызовется
z.test()