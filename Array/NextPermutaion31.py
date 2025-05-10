def nextPermutation(nums):
    n=len(nums)
    gola_index = -1
    for i in range(n-1,0,-1):
        if nums[i] > nums[i-1]:
            gola_index = i-1
            break
    
    if gola_index != -1:
        for j in range(n-1,gola_index,-1):
            if nums[j]  > nums[gola_index]:
                nums[gola_index],nums[j] = nums[j] , nums[gola_index]
                break
    nums[gola_index+1:] = reversed(nums[gola_index+1:])
nums=[1,2,3]
nextPermutation(nums)
print(nums)