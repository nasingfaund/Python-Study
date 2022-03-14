from random import randint


def bubbleSort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                #print(f'i: {nums[j]}, i+1:{nums[j + 1]}')
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                # print(nums)
    return nums


n = 5
nums = []

for i in range(n):
    nums.append(randint(1, 101))

nums = bubbleSort(nums)
print(nums)
