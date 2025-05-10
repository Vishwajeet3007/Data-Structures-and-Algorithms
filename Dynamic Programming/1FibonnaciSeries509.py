# # Using recursion and memo
# def rec(n,dp):
#     if  n <= 1:
#         return n
#     if dp[n] != -1:
#         return dp[n]
#     dp[n] = rec(n-1,dp) + rec(n-2,dp)
#     return dp[n]
# def fib(n):
#     dp = [-1] * (n+1)
#     return rec(n,dp)
# n = 7
# print(fib(n))

# Using Bottom-up
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
n = 7
print(fib(n))