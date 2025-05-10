def secondLargest(arr):
    first = float('-inf')
    second = float('-inf')
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] >  second and arr[i] < first:
            second = arr[i]
    return second
arr = [10,5,10]
print(secondLargest(arr))