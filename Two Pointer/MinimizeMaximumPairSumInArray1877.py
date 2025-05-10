def maxPairSum(nums):
    nums.sort()
    i = 0
    j = len(nums) - 1
    result = 0
    while i < j:
        summ = nums[i] + nums[j]
        result = max(result,summ)
        i += 1
        j -= 1
    return result
nums = [3,5,2,3]
print(maxPairSum(nums))
nums = [3,5,4,2,4,6]
print(maxPairSum(nums))