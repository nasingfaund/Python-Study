from test_functions import generate_list, test


def insertion_sort(numbers):

    result = [numbers[0]]

    for i in range(1, len(numbers)):

        result.append(numbers[i])
        j = len(result) - 1

        while j > 0:
            if result[j - 1] > result[j]:
                result[j], result[j - 1] = result[j - 1], result[j]
            j -= 1

    return result


# l = generate_list(10)
# print(l)
# print(insertion_sort(l))

# -------------------- TESTS ---------------------
test(insertion_sort)
