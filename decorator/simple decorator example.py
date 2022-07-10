def dec(*decargs):
    def outer(func):
        def inner(*args):
            args2 = list(args)
            args2 += decargs
            print(f'before {func.__name__} call')
            func(tuple(args2))
            print(f'after {func.__name__} call')

        return inner

    return outer


# добавляем параметры в сам декоратор
@dec(0, 'dec param')
def test(*args):
    for arg in args:
        print(arg)


# в итоге видим параметры, переданные непосредственно в функцию + параметры декоратора
test(1, '2', '33')