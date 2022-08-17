from test_functions import generate_list, get_exec_time


@get_exec_time
def get_fast(nums1, nums2):
    result = set()
    d = {x: None for x in nums1}

    for num in nums2:
        if num in d:
            result.add(num)

    return list(result)


@get_exec_time
def get_slow(nums1, nums2):
    result = []

    # если листы конвертировать в множества, то слоу вариант станет быстрее фаст варианта)
    # nums1 = set(nums1)
    # nums2 = set(nums2)
    for num in nums1:
        if num in nums2 and num not in result:
            result.append(num)

    return result


n = 10 ** 7
nums1 = generate_list(n)
nums2 = generate_list(n)

get_fast(nums1, nums2)
get_slow(nums1, nums2)
