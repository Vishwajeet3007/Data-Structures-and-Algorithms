def twoSum(arr,target):
    num_map = {}
    for i ,num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return [num_map[complement],i]
        num_map[num] = i
    return [-1,-1]
nums = [2, 7, 11, 15]
target = 9  
print(twoSum(nums,target))
