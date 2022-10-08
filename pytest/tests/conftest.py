import pytest
from functions import write_to_file

# https://www.youtube.com/watch?v=-4ag5I0_hZU&ab_channel=ITidea

"""
в файле conftest.py предназначен для фикстур
    фикстура подготавливает тестируемое окружения для тестов
    может вызываться и до и после тестов

для того, чтобы тест использовал фикстуру, можно просто передать
    фикстуру в качестве параметра (импорт фикстуры при этом не нужен!)

pytest распознает тестовые модули по паттерну в имени test_*.py или *_test.py,
    тестовые функции распознает по паттерну test_*

структура фикстуры:
    1. SETUP - шаг вызова ДО тест-метода
    2. yield (опционально) - оператор для передачи управления тест-методу
    3. TEARDOWN (опционально) - шаг вызова ПОСЛЕ тест-метода

команда запуска тестов с выводом принтов и конфигурации тестирования: 
    pytest -s <файл> --setup-show
-------------------------------------------------------------------------------------

                    ЗАДАЧА:
предположим, что нам нужно тестировать чтение из файла,
    но какой-то тест ранее заполнил файл своей информацией.
    в этом случае тестирование не пройдет корректно
    и нужно очищать файл перед запуском тестов.
    для таких целей и нужны фикстуры
"""

def external_teardown():
    print(' external teardown')

# параметр request описывает контекст вызванного теста
# запуск теста:
# pytest -s pytest/tests/test_file_reader.py::test_with_file --setup-show
@pytest.fixture
def flush_file_fixture(request):
    print(f'\n test of {request.function.__name__}')
    print('\n setup of flush_file')
    write_to_file('', 'w')
    yield
    print('\n teardown of flush_file')

    # teardown можно задать в виде отдельной функции
    request.addfinalizer(external_teardown)

