import time
import random

"""
ПИШЕМ ДЕКОРАТОР БЕЗ ПАРАМЕТРОВ ДЛЯ ЗАМЕРА ВРЕМЕНИ ВЫПОЛНЕНИЯ ФУНКЦИЙ РАЗВОРОТА ЧИСЛА
"""


# https://tproger.ru/translations/demystifying-decorators-in-python/

def get_exec_time(func):

    def inner(*args, **kwargs):
        inner.__name__ = func.__name__
        start_time = time.monotonic()
        result = func(*args, **kwargs)
        finish_time = time.monotonic()
        print(f'execution time of {func.__name__} is {round(finish_time - start_time, 2)} s.')
        return result

    return inner


# тупой алгоритм
@get_exec_time
def num_reverse_stupid(number):
    result = 0
    num_str = str(number)
    n = len(num_str)

    # идем с конца
    for i in range(n - 1, -1, -1):
        result += int(num_str[i]) * 10 ** i

    return result


# умный алгоритм
@get_exec_time
def num_reverse_good(number):
    result = 0

    while number >= 1:
        result = result * 10 + (number % 10)
        number //= 10

    return result


def generate_test_list(values_count):
    i = 1
    result = []

    while i != values_count:
        number = random.randint(10 ** 30, 10 ** 31 - 1)
        result.append(number)
        i += 1

    return result


# ----------------------------- TESTS ------------------------------------

num1 = 23429948362932032342066756853420667568534234206675685234206675685342342066756853434
num2 = 3458760707832223420699483629320323420667568534267568534234206675685347420223420667568
num3 = 9948362932032342342994836293203234206675685342066756853423420667568523420206675685342

assert str(num_reverse_stupid(num1)) == str(num1)[::-1]
assert str(num_reverse_stupid(num2)) == str(num2)[::-1]
assert str(num_reverse_stupid(num3)) == str(num3)[::-1]

assert str(num_reverse_good(num1)) == str(num1)[::-1]
assert str(num_reverse_good(num2)) == str(num2)[::-1]
assert str(num_reverse_good(num3)) == str(num3)[::-1]
