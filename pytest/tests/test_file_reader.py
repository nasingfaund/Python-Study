from functions import write_to_file, read_from_file


def test_with_file():
    """
    можно не передавать в параметры фикстуру flush_file_fixture,
    т.к. у нее есть параметр autouse=True (подробнее в conftest.py)
    """
    write_to_file('text')
    assert read_from_file() == 'text'
