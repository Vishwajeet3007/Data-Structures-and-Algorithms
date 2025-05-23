def findMiddleIndex(nums):
    total_sum = sum(nums)
    prefix_sum = 0
    for i in range(len(nums)):
        suffix_sum = total_sum - prefix_sum - nums[i]
        if prefix_sum == suffix_sum:
            return i
        prefix_sum += nums[i]
    return -1
nums = [2,3,-1,8,4]
print(findMiddleIndex(nums))