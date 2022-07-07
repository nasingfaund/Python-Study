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


# создаем класс с помощью метакласса type
# сам класс называется test, а объект с ссылкой на класс может называться как угодно
class_obj = type('test', (), {
    'attr1': None,
    '__init__': init_func,
    'print_attrs': print_attrs
})

# отрабатывают конструктор и метод print_attrs
obj = class_obj('attr1 value', 'attr2 value')
obj.print_attrs()

