def getIntersection(nums1, nums2):
    result = []
    dict = {}

    for x in nums2:
        dict[x] = None

    for x in nums1:
        if x in dict and x not in result:
            result.append(x)

    return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = getIntersection(nums1, nums2)
print(result)