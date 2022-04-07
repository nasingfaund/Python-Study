import copy

from test_functions import generate_list, test


def find_min(numbers):
    min = numbers[0]
    min_index = 0

    for i in range(len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
            min_index = i

    return min, min_index


# все вручную (включая поиск минимума)
def stupid_sort(numbers):
    result = []
    numbers_copy = copy.copy(numbers)

    for i in range(len(numbers_copy)):
        min_value, min_index = find_min(numbers_copy)
        result.append(min_value)
        numbers_copy.pop(min_index)

    return result


# нативный поиск минимума
def stupid_sort_upgraded(numbers):
    result = []
    numbers_copy = copy.copy(numbers)

    for i in range(len(numbers_copy)):
        min_value = min(numbers_copy)
        min_index = numbers_copy.index(min_value)
        result.append(min_value)
        numbers_copy.pop(min_index)

    return result


# l = generate_list(10)
# print(l)
# print(stupid_sort(l))

# -------------------- TESTS ---------------------
test(stupid_sort)  # stupid_sort stupid_sort_upgraded sorted
