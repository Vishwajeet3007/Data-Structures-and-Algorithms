def getPairs(arr):
    arr.sort()
    n = len(arr)
    pairs = set()
    left = 0
    right = n - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == 0:
            pairs.add((arr[left],arr[right]))
            left += 1
            right -= 1
        elif total < 0:
            left += 1
        else: 
            right -= 1
    return sorted(pairs)
arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
print(getPairs(arr))

arr = [-1, 0, 1, 2, -1, -4]
print(getPairs(arr))