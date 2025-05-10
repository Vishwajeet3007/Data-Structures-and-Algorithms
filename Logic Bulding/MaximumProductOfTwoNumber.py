def maxProductOfTwoNumber(arr):
    # first Method
    # maxProd = 0
    # for i in range(len(arr)-1):
    #     for j in range(i+1,len(arr)):
    #         maxProd = max(maxProd,arr[i] * arr[j])
    # return maxProd

    #second Method 
    # arr.sort()
    # return arr[-1] * arr[-2]

    # third method 
    first = float('-inf')
    second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return first * second

print(maxProductOfTwoNumber([3, 7, 2, 8, 5]))
print(maxProductOfTwoNumber([1, 10, 3, 9]))