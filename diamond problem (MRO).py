"""
Порядок разрешения методов
Method Resolution Order - MRO
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


# если поменять порядок наследования,
# результат getInfo() изменится
class D(C, B):
    pass

# MRO - алгоритм поиска в ширину:
# сначала интерпретатор будет искать метод getInfo
# в классе C (если наследоваться в порядке C, B) или в B
# (если наследоваться в порядке B, C), а затем в классе A


d = D()
d.getInfo()
print(D.mro())
