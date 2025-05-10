def maxSubArraySum(arr):
    curr_sum = arr[0]
    max_sum = arr[0]
    for i in range(1,len(arr)):
        curr_sum = max(arr[i],arr[i] + curr_sum)
        max_sum = max(max_sum , curr_sum)
    return max_sum
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArraySum(arr))