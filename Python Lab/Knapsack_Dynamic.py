def knapsack(values, weights, max_weight):
    n = len(values)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # The maximum value is in dp[n][max_weight]
    return dp[n][max_weight]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
max_weight = 50
print("Maximum value in Knapsack:", knapsack(values, weights, max_weight))
