'''
Написать параметризированный декоратор,
который печатает время выполнения декорированной функции.
Параметр декоратора — печатать время выполнения в секундах или в миллисекундах.
'''
import time


def func():
    time.sleep(3)


start_time = time.monotonic()
func()
finish_time = time.monotonic()
print(f'exec time: {finish_time - start_time} seconds')
