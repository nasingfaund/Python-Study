def RLE(inputStr):
    result = ''
    count = 1

    for i in range(0, len(inputStr)):

        letter = inputStr[i]

        # чек IndexOutOfRange
        if i + 1 > len(inputStr) - 1:
            result += letter if count == 1 else letter + str(count)
            break

        nextLetter = inputStr[i + 1]

        if letter == nextLetter:
            count += 1
        else:
            result += letter if count == 1 else letter + str(count)
            count = 1

    return result

def deRLE(str):
    result = ''
    number = ''

    for i in range(0, len(str)):
        letter = str[i]

        # чек IndexOutOfRange
        if i + 1 > len(str) - 1:
            if number == '':
                result += letter
            else:
                letterIndex = i - len(number)
                result += str[letterIndex] * int(number)
            break

        nextLetter = str[i + 1]

        if nextLetter.isdigit():
            number += nextLetter
        else:
            if number == '':
                result += letter
            else:
                letterIndex = i - len(number)
                result += str[letterIndex] * int(number)
                number = ''

    return result


encryptTests = {
    'ABCCDEEF': 'ABC2DE2F',
    'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB': 'A4B3C2XYZD4E3F3A6B28',
    'AAAABBBCCXYZDDDDEEEFFFAAAAAABCSSSSDDC': 'A4B3C2XYZD4E3F3A6BCS4D2C'
}

decryptTests = {
    'ABC2DE2F': 'ABCCDEEF',
    'A4B3C2XYZD4E3F3A6B28': 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'A4B3C2XYZD4E3F3A6BCS4D2C': 'AAAABBBCCXYZDDDDEEEFFFAAAAAABCSSSSDDC',
    'ABCDE' : 'ABCDE'
}
def encryptTest():
    for s in encryptTests:
        assert RLE(s) == encryptTests[s]
        print(f'RLE({s}) = {RLE(s)}')

def decryptTest():
    for s in decryptTests:
        assert deRLE(s) == decryptTests[s]
        print(f'deRLE({s}) = {deRLE(s)}')
