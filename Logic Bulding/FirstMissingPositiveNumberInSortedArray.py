def findMissingPositiveNumber(arr):
    result = [num for num in arr if num > 0]
    for i in range(len(result)):
        if result[i] != i + 1:
            return i + 1
    return len(result) + 1

# def findMissingPositiveNumber(arr):
#     n = len(arr)
#     for i in range(n):
#         while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
#             arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]  # Swap elements

#     for i in range(n):
#         if arr[i] != i + 1:
#             return i + 1  # First missing positive

#     return n + 1  # If all numbers are in order

arr = [1, 2, 3, 5, 6, 7]
print(findMissingPositiveNumber(arr))  # Output: 4

arr = [-3, -1, 0, 1, 2, 4]
print(findMissingPositiveNumber(arr))  # Output: 3

arr = [1, 2, 3, 5, 6, 7]
print(findMissingPositiveNumber(arr))
arr = [-3, -1, 0, 1, 2, 4]
print(findMissingPositiveNumber(arr)) 

            