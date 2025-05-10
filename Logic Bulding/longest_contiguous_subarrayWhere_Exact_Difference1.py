def longest_contiguous_subarray(arr):
    if not arr:
        return 0
    max_len = 1
    current_len = 1
    for i in range(1,len(arr)):
        if abs(arr[i] - arr[i-1]) == 1:
            current_len += 1
        else:
            max_len = max(max_len,current_len)
            current_len = 1
    return max(max_len,current_len)
    
arr =  [10, 9, 4, 5, 6, 7, 8, 1, 2, 3, 2, 1]
print(longest_contiguous_subarray(arr))


