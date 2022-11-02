# region 1 способ - реализация методов __enter__ и __exit__ в классе, объект которого будет использован
class Resource:

    def action(self):
        print('do something...')

    # enter должен возвращать тип/объект
    def __enter__(self):
        return self

    # exit вызывает освобождение ресурса
    def __exit__(self, type, value, traceback):
        print('close resource')


res = Resource()

# теперь менеджер управляет созданием объекта и его высвобождением
with res:
    res.action()
print('-------------------------------------')
# endregion

# region 2 способ - использование модуля contextlib (через декораторы)
from contextlib import contextmanager
import os.path


# декорируем функцию
@contextmanager
def file_open(filepath):
    """ до yield - аналог __enter__() """
    if not os.path.exists(filepath):
        f_obj = open(filepath, 'w+')

    f_obj = open(filepath, 'w')
    yield f_obj

    """ после yield - аналог __exit__() """
    if f_obj is not None:
        f_obj.close()
        print('file has been closed')


with file_open('test.txt'):
    pass
# endregion
