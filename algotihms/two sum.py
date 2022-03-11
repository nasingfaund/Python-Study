def twoSum(nums, target):

    for i in range(0, len(nums)):
        second = target - nums[i]

        if second in nums:
            secondIndex = nums.index(second)

            if secondIndex != i:
                return [secondIndex, i]

    return []


nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))
