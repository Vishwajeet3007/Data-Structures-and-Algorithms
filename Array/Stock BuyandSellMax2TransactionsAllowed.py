def StockBuyandSellMax2TransactionsAllowed(arr):
    if not arr or len(arr) == 1:
        return 0
    n=len(arr)
    selling = arr[0]
    profit = [0] * n
    for i in range(n-2,-1,-1):
        if selling > arr[i]:
            selling = arr[i]
        profit[i] = max(profit[i+1],selling-arr[i])
    
    buying = arr[0]
    for i in range(1,n):
        if arr[i] < buying:
            buying = arr[i]
        profit[i] = max(profit[i-1],profit[i]+(arr[i]-buying))
    return profit[n-1]
arr = [2, 30, 15, 10, 8, 25, 80]
result =  StockBuyandSellMax2TransactionsAllowed(arr)
print(result)
