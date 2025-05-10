def secondLargest(arr):
    if len(arr) < 2:
        return "Array must have at least two distinct elements."
    first = float('-inf')  # Smallest possible value
    second = float('-inf') 
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second:
            second = arr[i]
    return second
arr = [4,56,7,4,26,77]
result = secondLargest(arr)
print("Second Larget : ",result)
