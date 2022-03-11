"""
Написать параметризированный декоратор,
который печатает время выполнения декорированной функции.
Параметр декоратора — печатать время выполнения в секундах или в миллисекундах.
"""

import time
from enum import Enum


class TimeFormat(Enum):
    Seconds = 's'
    Milliseconds = 'ms'


# фукнция-обертка для вычисления время выполнения функции execFunc
# код этой функции можно было разместить внутри декоратора (в inner),
# но для удобства вынесено отдельно
def getFuncExecTime(execFunc, timeValue, resultFormat):
    start_time = time.monotonic()
    execFunc(timeValue)
    finish_time = time.monotonic()
    # отбросим дробную часть, образованную в результате погрешностей
    execTime = (finish_time - start_time) // 1
    # тернарный оператор
    return execTime if resultFormat == TimeFormat.Seconds else execTime * 100


def decoratorFunc(timeFormat):
    def outer(execFunc):
        def inner(timeValue):
            execTime = getFuncExecTime(execFunc, timeValue, timeFormat)
            print(f'exec time: {execTime} {str(timeFormat)}')
            # return execTime

        return inner

    return outer


@decoratorFunc(TimeFormat.Milliseconds)
def someProcess(timeValue):
    time.sleep(timeValue)


@decoratorFunc(TimeFormat.Seconds)
def someProcess2(timeValue):
    time.sleep(timeValue)


someProcess2(3)

#
