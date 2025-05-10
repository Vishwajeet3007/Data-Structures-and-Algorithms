def rob(nums):
    # Using Bottom-Up 
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * (n+1)
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2,n):
        steal = nums[i] + dp[i-2]
        skip = dp[i-1]
        dp[i] = max(steal,skip)
    return dp[n-1]
n = [1,2,3,1]
print(rob(n))
n = [2,7,9,3,1]
print(rob(n))
