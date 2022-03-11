# задача: разбить лист numbers на указаное количество частей (чанков)

# generator solution (разбиваем по количеству чанков)

def chunksGenerate(numbers, chunksCount):
    chunksSize = len(numbers) // chunksCount
    startIndex = 0
    endIndex = chunksSize

    while endIndex <= len(numbers):
        yield numbers[startIndex:endIndex]
        startIndex += chunksSize
        endIndex += chunksSize


chunksCount = 4
numbers = list(range(1, 101))

chunkFunc = chunksGenerate(numbers, chunksCount)
# print(next(chunkFunc))
# print(next(chunkFunc))
# print(next(chunkFunc))
# print(next(chunkFunc))


def test(x):
    yield x + 1
    yield x + 2
    return
    # недостижимый код
    yield x + 3

t = test(10)
print(next(t))
print(next(t))
# следующее выполнение генератора даст исключение StopIteration
#print(next(t))
