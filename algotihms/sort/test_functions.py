import random as rnd
import time


def generate_list(n):
    return [rnd.randint(-99, 100) for i in range(n)]


def get_exec_time(func):
    def inner(*args):
        inner.__name__ = func.__name__
        start_time = time.time()
        func(*args)
        finish_time = time.time()
        print(f'execution time: {round(finish_time - start_time, 2)} seconds')

    return inner


ELEMENTS_COUNT = 2000
TESTS_COUNT = 50


@get_exec_time
def test(sort_algo):
    for i in range(TESTS_COUNT):

        test_list = generate_list(ELEMENTS_COUNT)

        try:
            assert sort_algo(test_list) == sorted(test_list)
            print(f'test {i + 1}/{TESTS_COUNT} ({ELEMENTS_COUNT} elements): passed')
        except:
            print(f'error on test №{i + 1}, elements count = {ELEMENTS_COUNT}')
            return

    print(f'{sort_algo.__name__} successfully passed all tests.')
    print(f'\ntotal number of sorted items: {ELEMENTS_COUNT * TESTS_COUNT}')
