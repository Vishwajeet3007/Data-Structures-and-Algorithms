def longestConsecutiveSubarray(arr):
    s = set(arr)
    ans = 0
    for i in range(len(arr)):
        if (arr[i]-1) not in s:
            j = arr[i]
            while j in s:
                j += 1
            ans = max(ans,j-arr[i])
    return ans
arr = [4,7,9,8,5,3,2,1]
result = longestConsecutiveSubarray(arr)
print(result) 