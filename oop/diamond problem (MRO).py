"""
Порядок разрешения методов (Method Resolution Order - MRO)
"""
class A:
    def getInfo(self):
        print('A')

class B(A):
    def getInfo(self):
        print('B')

class C(A):
    def getInfo(self):
        print('C')

class D(C, B):
    pass

D().getInfo()
print(D.mro())

# пример 2 (в этих случаях вывод будет в обратном порядке по MRO)

class A:
    def __init__(self):
        print('class A')


class B(A):
    def __init__(self):
        super().__init__()
        print('class B')


class C(A):
    def __init__(self):
        super().__init__()
        print('class C')


class Test(B, C):
    def __init__(self):
        super().__init__()
        print('class Test')

# вывод будет идти в обратном порядке по mro (см. результат принта mro)
# то есть в обратном порядке по очереди наследования: Test(B, C)...А
# получаем линейный вид иерархии: Test <- B <- C <- A
# вывод в обратном порядке: A -> C -> B -> Test
Test()
print(Test.mro())