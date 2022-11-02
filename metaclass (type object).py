"""
https://www.youtube.com/watch?v=tp_cGBN_SQA&list=WL&index=27&ab_channel=selfedu
"""

# определяем конструктор
def init_func(object, arg1, arg2):
    object.attr1 = arg1
    object.attr2 = arg2


# определим обычный метод класса с выводом значений всех атрибутов
def print_attrs(self):
    for k, v in self.__dict__.items():
        print(f'{k}: {v}')


""" 
создаем класс с помощью метакласса type
параметры:
    1 - имя класса
    2 - кортеж классов, от которых хотим унаследоваться
    3 - словарь со значениями атрибутов класса
"""
TestClass = type('test', (), {
    'attr1': None,
    '__init__': init_func,
    'print_attrs': print_attrs
})

# отрабатывают конструктор и метод print_attrs
obj = TestClass('attr1 value', 'attr2 value')
obj.print_attrs()

