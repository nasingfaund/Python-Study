# создание своего контекстного менеджера
# 1 способ - реализация методов __enter__ и __exit__
class Resource:
    def __init__(self, name):
        print(f'create resource: {name}')
        self.__name = name

    def get_name(self):
        return self.__name

    # кастомная логика освобождения ресурса
    def close(self):
        print('close resource')


class ResourceWith:
    def __init__(self, name):
        self.__resource = Resource(name)

    # enter должен возвращать ресурс
    def __enter__(self):
        return self.__resource

    # exit освобождает ресурс
    def __exit__(self, type, value, traceback):
        self.__resource.close()


# теперь менеджер управляет созданием объекта и его высвобождением
with ResourceWith('res') as r:
    print(r.get_name())


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
    except OSError as e:
        print(e)
    finally:
        print('Closing file')
        if f_obj is not None:
            f_obj.close()


with file_open('test.txt') as file:
    file.write('Testing context managers')