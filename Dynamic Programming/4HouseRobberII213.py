def houseRobber(nums):
    def rob_linear(houses):
        n = len(houses)
        if n == 0:
            return 0
        if n == 1:
            return houses[0]
        dp = [0] * n
        dp[0] = houses[0]
        dp[1] = max(houses[0] , houses[1])
        for i in range(2,n):
            steal = houses[i] + dp[i-2]
            skip = dp[i-1]
            dp[i] = max(steal , skip)
        return dp[-1]
    n = len(nums)
    if n == 0:
        return 0
    if  n == 1:
        return nums[0]
    if n == 2:
        return max(nums)
    return max(rob_linear(nums[:-1]) , rob_linear(nums[1:]))
nums = [1,2]
print(houseRobber(nums))
nums = [1,2,3,1]
print(houseRobber(nums))
nums = [1,2,3]
print(houseRobber(nums))