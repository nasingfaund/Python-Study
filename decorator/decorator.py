"""
Написать ПАРАМЕТРИЗОВАННЫЙ декоратор,
который печатает время выполнения декорированной функции.
Параметр декоратора — печатать время выполнения в секундах или в миллисекундах.
"""

import time
from enum import Enum


class TimeFormat(Enum):
    Seconds = 's'
    Milliseconds = 'ms'


# фукнция-декоратор с параметром
def decoratorFunc(time_format):
    # декорируемая функция
    def outer(exec_func):
        # параметры для декорируемой функции
        def inner(*args):
            start_time = time.monotonic()
            exec_func(*args)
            finish_time = time.monotonic()
            # отбросим дробную часть, образованную в результате погрешностей
            exec_time = (finish_time - start_time) // 1
            # тернарный оператор
            exec_time = exec_time if time_format == TimeFormat.Seconds else exec_time * 1000
            print(f'exec time: {exec_time} {str(time_format)}')

        return inner

    return outer


# это параметризованный декоратор (именно сам декоратор, т.к.
# в его аннотации есть передача параметра. вообще можно сделать без параметров)
@decoratorFunc(TimeFormat.Milliseconds)
def someProcess(timeValue):
    time.sleep(timeValue)


@decoratorFunc(TimeFormat.Seconds)
def someProcess2(timeValue):
    time.sleep(timeValue)


someProcess(3)
