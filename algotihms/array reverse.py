def reverse(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums


nums = list(reversed(range(1, 11)))
print(nums)
nums = reverse(nums)
print(nums)
