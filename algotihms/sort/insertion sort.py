from test_functions import generate_list, test


def insertion_sort(numbers):
    n = len(numbers)
    current_index = 2
    sorted_part = numbers[0:current_index]

    while True:

        i = len(sorted_part) - 1

        # сортируем с конца "отсортированный" подмассив
        while i != 0:
            if sorted_part[i] < sorted_part[i - 1]:
                sorted_part[i], sorted_part[i - 1] = sorted_part[i - 1], sorted_part[i]
            i -= 1

        if current_index > n - 1:
            break

        sorted_part.append(numbers[current_index])
        current_index += 1
        # print(f'sorted: {sorted_part}')

    return sorted_part


# l = generate_list(10)
# print(l)
# print(insertion_sort(l))

# -------------------- TESTS ---------------------
test(insertion_sort)
