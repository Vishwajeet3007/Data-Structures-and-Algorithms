"""Given an integer array nums, return the number of subarrays of length 3
 such that the sum of the first and third numbers equals exactly half of the 
 second number."""
def countSubarrays(nums):
    count = 0
    for i in range(1,len(nums) - 1):
        if 2 * (nums[i-1] + nums[i+1]) == nums[i]:
            count += 1
    return count
nums = [1,2,1,4,1]
print(countSubarrays(nums))
nums = [1,1,1]
print(countSubarrays(nums))
