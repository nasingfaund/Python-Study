import pytest


def func(a, b: float) -> float:
    return a / b


@pytest.mark.parametrize('a, b, expected_result', [
    (10, 2, 5),
    (-5, 2, -2.5),
    (-6, -3, 2),
])
# функция-тест обязательно должна начинаться с "test"
def test_true(a, b, expected_result):
    assert func(a, b) == expected_result


@pytest.mark.parametrize('a, b, exception_class', [
    ('s', 5, TypeError),
    (5, 0, ZeroDivisionError),
])
def test_false(a, b, exception_class):
    with pytest.raises(exception_class):
        func(a, b)
