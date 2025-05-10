def arrayLeader(arr):
    result = []
    max_right = float('-inf')
    for i in range(len(arr)-1,-1,-1):
        if arr[i] >= max_right:
            max_right = arr[i]
            result.append(arr[i])
    return result[::-1]
print(arrayLeader([16, 17, 4, 3, 5, 2]))
print(arrayLeader([1, 2, 3, 4, 5]))
print(arrayLeader([10, 9, 8, 7]))
print(arrayLeader([5, 10, 20, 40]))
print(arrayLeader([30, 10, 10, 5]))