def unit_print():
    print(f'unit method call, __name__={__name__}')


# БЕЗ УСЛОВИЯ: при импорте в example.py метод отработает
# unit_print()

""" С УСЛОВИЕМ:
при импорте в example.py в модуле example переменная __name__ получит значение не __main__, а unit
таким образом вызываемые здесь методы не будут вызваны при импорте в других модулях!
"""
if __name__ == '__main__':
    unit_print()
