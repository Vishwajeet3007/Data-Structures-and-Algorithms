def maxSubarrayProduct(arr):
    max_prodct = arr[0]
    product = arr[0]
    min_product = arr[0]

    for i in range(1,len(arr)):
        if arr[i] < 0:
            max_prodct,min_product=min_product,max_prodct
        max_prodct = max(arr[i],max_prodct * arr[i])
        min_product = min(arr[i],min_product * arr[i])
        product = max(product,max_prodct)
    return product
arr = [6,-3,-10,0,2]
result = maxSubarrayProduct(arr)
print("Maximum product of subarray : ",result) 