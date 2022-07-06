import random as rnd


class Generator:

    def __init__(self):
        self.list = [i + 1 for i in range(1, 11)]  # [rnd.randint(1, 10) for i in range(1, 11)]
        self.current = -1

    def __next__(self):
        self.current += 1

        if self.current > len(self.list) - 1:
            raise StopIteration

        return self.list[self.current]

    def __iter__(self):
        return self

    def gen(self):

        if self.current == -1:
            self.current = 0

        while self.current < len(self.list):
            yield self.list[self.current]
            self.current += 1


gen = Generator()

for x in gen:
    print(x, end=' ')

gen_obj = Generator().gen()
print('\n')

for i in range(10):
    print(next(gen_obj), end=' ')