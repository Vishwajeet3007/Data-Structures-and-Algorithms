def findMissingNumber(arr):
    n = len(arr)
    total_sum = n*(n+1)//2
    actual_sum = sum(arr)
    return total_sum - actual_sum
arr = [1,0,4,7,2,3,5]
print(findMissingNumber(arr))
arr = [0,1,2]
print(findMissingNumber(arr))