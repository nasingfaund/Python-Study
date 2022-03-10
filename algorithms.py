# поиск двумя указателями
def searchByPointers(nums, target):
    a = 0
    b = len(nums) - 1

    while a <= b:

        if nums[a] == target:
            return a

        if nums[b] == target:
            return b

        if target < nums[b]:
            b -= 1
        else:
            a += 1

    return -1

# бинарный поиск
def binarySearch(nums, target):
    a = 0
    b = len(nums) - 1

    while a <= b:

        mid = (a + b) // 2

        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            b = mid - 1
        else:
            a = mid + 1

    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 5
print(searchByPointers(nums, target))
