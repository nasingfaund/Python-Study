def isValid(s):

    if len(s) % 2 != 0:
        return False

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for bracket in s:
        if bracket in '([{':
            stack.append(bracket)
        else:

            # как минимум в стеке должна лежать хотя бы одна скобка
            if len(stack) == 0:
                return False

            lastStackBracket = stack.pop()

            if pairs[bracket] != lastStackBracket:
                return False

    return len(stack) == 0

s = '){'
print(isValid(s))
