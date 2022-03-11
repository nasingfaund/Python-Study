# поиск индекса указнного числа двумя указателями
def twoPointersSearch(nums, target):
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

nums = [-1, 0, 3, 5, 9, 12]
target = 5
print(twoPointersSearch(nums, target))