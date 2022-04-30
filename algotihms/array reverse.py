import copy


def reverse(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums


nums = list(range(1, 11))
nums_1 = copy.copy(nums)
assert reverse(nums_1) == list(reversed(nums))
