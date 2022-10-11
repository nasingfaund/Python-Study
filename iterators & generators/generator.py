"""
    задача: разбить лист numbers на указаное количество частей (чанков)
    generator function solution (разбиваем по количеству чанков)
"""


# 1. ФУКНЦИЯ-ГЕНЕРАТОР
def chunksGenerate(numbers, chunks_count):
    chunks_size = len(numbers) // chunks_count
    startIndex = 0
    endIndex = chunks_size

    while endIndex <= len(numbers):
        yield numbers[startIndex:endIndex]
        startIndex += chunks_size
        endIndex += chunks_size


chunksCount = 4
numbers = list(range(1, 101))

chunkFunc = chunksGenerate(numbers, chunksCount)

print(next(chunkFunc))
print(next(chunkFunc))
print(next(chunkFunc))
print(next(chunkFunc))

print('\ngen_func:')


def gen_func(x):
    while True:
        x = yield
        x += 5
        print(x, end=' ')


g = gen_func(5)
next(g)
g.send(3)
g.send(6)
g.close()

# 2. ГЕНЕРАТОРНОЕ ВЫРАЖЕНИЕ
print('\ngenexpr:')
genexpr = (x ** 2 for x in range(1, 5))
[print(v, end=' ') for v in genexpr]
