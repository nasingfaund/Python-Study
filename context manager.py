# создание своего контекстного менеджера
# 1 способ - реализация методов __enter__ и __exit__
class Resource:
    def __init__(self, name):
        print(f'create resource: {name}')
        self.__name = name

    def action(self):
        print('do something...')

    # логика освобождения ресурса
    def __close(self):
        print('close resource')

    # enter должен возвращать тип/объект
    def __enter__(self):
        return self

    # exit вызывает освобождение ресурса
    def __exit__(self, type, value, traceback):
        self.__close()


res = Resource('resource')

# теперь менеджер управляет созданием объекта и его высвобождением
with res:
    res.action()
print('-------------------------------------')


# 2 способ - использование модуля contextlib (через декораторы)
from contextlib import contextmanager
import os.path


# декорируем нашу функцию
@contextmanager
def file_open(filepath):
    f_obj = None

    try:

        if not os.path.exists(filepath):
            f_obj = open(filepath, 'w+')

        f_obj = open(filepath, 'w')
        yield f_obj

    finally:
        if f_obj is not None:
            f_obj.close()
            print('file has been closed')


with file_open('test.txt') as file:
    file.write('Testing context managers')
