"""
https://www.youtube.com/watch?v=_A90qAV_P5U&list=WL&index=28&t=4s&ab_channel=selfedu
"""


class Meta(type):

    def __new__(cls, name, base, attrs):
        attrs.update({
            'attr1': 1,
            'attr2': 2
        })
        return type.__new__(cls, name, base, attrs)


class test_class(metaclass=Meta):
    def func(self):
        print(self.func.__name__)


obj = test_class()
obj.func()
print(obj.attr1, obj.attr2)



