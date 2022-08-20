"""
monkey patching позволяет
динамически обновлять поведение кода во время выполнения
в частности делать моки в рамках тестирования
"""
import time


def mock_load_page(*args, **kwargs):
    return 'page'


""" 
ОПИСАНИЕ ПРОБЛЕМЫ: 
мы хотим протестировать только парсинг, а еще не хотим долго ждать результата из load_page
а вдруг оригинальный load_page по какой-то причине не вернет результат?
для этого и замокаем его с помощью monkeypatch
monkeypatch умеет подменять значения в словарях, классах, переменных окружений и т.д.
"""


def test_parse(monkeypatch):
    # мокаем метод load_page
    monkeypatch.setattr('mock.AbstractParser.load_page', mock_load_page)
    parser = AbstractParser()
    assert parser.parse('url') == f'page parsed from url'


class AbstractParser:

    # типа очень долго работающая функция
    def load_page(self, url):
        time.sleep(10000)
        return 'page'

    def parse(self, url):
        page = self.load_page(url)
        # do something (parse)
        return f'{page} parsed from {url}'
