def max_profit(prices):
    if not prices:
        return 0 
    min_purchase = prices[0]
    max_profit = 0
    for val in prices:
        temp = val - min_purchase
        if temp > max_profit:
            max_profit = temp
        if val < min_purchase:
            min_purchase = val
    return max_profit
print(max_profit([7,1,5,3,6,4]))  # Output: 5 (Buy at 1, Sell at 6)
print(max_profit([7,6,4,3,1]))    # Output: 0 (No profitable transactions)
print(max_profit([]))             # Output: 0 (Handles empty list safely)


