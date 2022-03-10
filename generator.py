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

# function solution (разбиваем по размеру чанка)

def getChunks(numbers, chunkSize):
    chunksCount = len(numbers) // chunkSize
    chunks = []
    startIndex = 0
    endIndex = chunkSize
    currentChunkNumber = 1

    while currentChunkNumber <= chunksCount:
        chunks.append(numbers[startIndex:endIndex])
        startIndex = currentChunkNumber * chunkSize
        endIndex += chunkSize
        currentChunkNumber += 1

    return chunks


chunksCount = 4
numbers = list(range(1, 101))

chunkFunc = chunksGenerate(numbers, chunksCount)
print(next(chunkFunc))
print(next(chunkFunc))
print(next(chunkFunc))
print(next(chunkFunc))

chunkSize = 5
chunks = getChunks(numbers, chunkSize)
for chunk in chunks:
    print(chunk)