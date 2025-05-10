def firstMissing(arr):
    n = len(arr)
    for i in range(n):
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i]-1]:
            temp = arr[i]
            arr[i] = arr[arr[i] -1 ]
            arr[temp - 1] = temp
    for i in range(n):
        if arr[i] != i + 1:
            return i+1
    return n + 1 
print(firstMissing([3, 4, -1, 1]))  
print(firstMissing([1, 2, 0]))      
print(firstMissing([7, 8, 9, 11, 12])) 
        