import pytest

FILENAME = 'f.txt'


def write_to_file(text, mode='a'):
    with open(FILENAME, mode) as file:
        file.write(text)


def read_from_file():
    with open(FILENAME, 'r') as file:
        return file.read()


@pytest.mark.parametrize('text, expected_value', [
    ('text', 'text'),
])
def test_false(text, expected_value):
    write_to_file(text)
    assert read_from_file() == expected_value
