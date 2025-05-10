def numSubSeqeunce(nums,target):
    nums.sort()
    n = len(nums)
    left , right = 0 , n - 1
    power = [1] * n
    mod = 10 ** 9 + 7
    result = 0
    for i in range(1,n):
        power[i] = (power[i-1] * 2) % mod
    while left <= right:
        if nums[left] + nums[right] <= target:
            result = (result % mod + power[right - left]) % mod
            left += 1
        else:
            right -= 1
    return result
nums = [3,5,6,7]
target = 9
print(numSubSeqeunce(nums,target))
nums = [2,3,3,4,6,7]
target = 12
print(numSubSeqeunce(nums,target))
nums = [3,3,6,8]
target = 10
print(numSubSeqeunce(nums,target))
            