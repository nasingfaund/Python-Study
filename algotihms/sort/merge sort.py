from test_functions import generate_list, test


def merge_sort(numbers):
    splitted_list = []

    for i in range(len(numbers) - 1):
        l = [numbers[i], numbers[i + 1]]
        splitted_list.append(l)


l = generate_list(10)
print(l)
print(merge_sort(l))

# -------------------- TESTS ---------------------
# test(100, merge_sort)
