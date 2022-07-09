gen_expression = (x ** 2 for x in range(11) if x % 2 == 0 and x > 0)

print('gen_expression values:')
for v in gen_expression:
    print(v)


def gen_function():
    x = 0
    while x < 11:
        if x % 2 == 0 and x > 0:
            yield x ** 2
        x += 1


print('gen_function values:')
gen = gen_function()
for v in gen:
    print(v)