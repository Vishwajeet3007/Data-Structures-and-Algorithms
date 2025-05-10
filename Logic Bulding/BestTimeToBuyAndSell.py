def maxProfit(prices):
    n = len(prices)
    maxValue = [0] * n
    maxValue[n-1] = prices[n-1]
    for i in range(n-2,-1,-1):
        maxValue[i] = max(maxValue[i+1],prices[i])
    ans = 0
    for i in range(n):
        currProfit = maxValue[i] - prices[i]
        ans = max(currProfit,ans)
    return ans
print(maxProfit([7,1,5,3,6,4]))