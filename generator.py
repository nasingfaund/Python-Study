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

# ГЕНЕРАТОРЫ БЫВАЮТ ДВУХ ТИПОВ
# 1. ФУКНЦИЯ-ГЕНЕРАТОР

def test(x):
    yield x + 1
    yield x + 2
    yield x + 5
    return
    # недостижимый код
    yield x + 3

t = test(10)
print(next(t))
print(next(t))
print(next(t))
# следующее выполнение генератора даст исключение StopIteration
#print(next(t))

# 2. ГЕНЕРАТОРНОЕ ВЫРАЖЕНИЕ
genexpr = (x**2 for x in range(1,5))
print(next(genexpr))
print(next(genexpr))
print(next(genexpr))
print(next(genexpr))

