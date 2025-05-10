def min_coins(coins, amount):
    # Initialize the dp array to a value greater than the possible minimum number of coins
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: No coins needed to make amount 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11
print("Minimum number of coins needed:")
print(min_coins(coins, amount))
