tests = {
    ('abbbbaaa', 'abbb'): (0, 3),
    ('string', 'str'): (0, 2)
}


def get_substr(s, sub_str):
    counter, start = 0, 0
    word_pointer, sub_pointer = 0, 0

    while word_pointer <= len(s) - 1:
        word_ch = s[word_pointer]
        sub_ch = sub_str[sub_pointer]

        if word_ch == sub_ch:
            counter += 1
            sub_pointer += 1

            if counter == 0:
                start = word_pointer
        else:
            counter = 0
            sub_pointer = 0

        if counter == len(sub_str):
            return start, word_pointer

        word_pointer += 1

    return -1, -1

word = 'naiveStringMatcher'
result = get_substr(word, 'e')
sub_str = word[result[0]: result[1] + 1] if result != (-1, -1) else 'nope'
print(sub_str)

# for s in tests:
#     assert get_substr(s[0], s[1]) == (tests[s][0], tests[s][1])
