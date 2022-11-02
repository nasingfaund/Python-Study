from string import ascii_letters

# dict comprehension - {key: value}
d = {k: ascii_letters[k] for k in range(11)}

# list comprehension
l = [x for x in range(2, 17) if x % 2 == 0]

# set comprehension
s = {x for x in range(10)}


# dict unpack example
class test:
    f1 = f2 = f3 = None

    def __init__(self, f1, f2, f3):
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3


params = {
    'f1': 3,
    'f2': 2,
    'f3': 22
}

o = test(**params)
print(o.__dict__)