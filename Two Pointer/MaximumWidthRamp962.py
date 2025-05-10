def maxWidthRamp(nums):
    # Using Brute Force
    # ramp = 0
    # for i in range(len(nums)-1):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] <= nums[j]:
    #             ramp = max(ramp,j-i)
    # return ramp

     # Using Two Pointers
    n = len(nums)
    rightMax = [0] * n
    rightMax[n-1] = nums[n-1]
    for i in range(n-2,-1,-1):
        rightMax[i] = max(rightMax[i+1],nums[i])
    ramp = 0
    i = 0 # pointer in nums
    j = 0 # pointers in rightMax
    while j < n:
        while i < j and nums[i] > rightMax[j]:
            i += 1
        ramp = max(ramp,j - i)
        j += 1
    return ramp
nums = [6,0,8,2,1,5]
print(maxWidthRamp(nums))
nums = [9,8,1,0,1,9,4,0,4,1]
print(maxWidthRamp(nums))