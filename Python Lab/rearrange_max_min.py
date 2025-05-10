"""
Write a python program for rearrange an array in maximum and minimum
 form using two pointers technique
"""
def rearrange_max_min(arr):
    # Sort the array in non-decreasing order
    arr.sort()

    # Initialize two pointers
    left = 0
    right = len(arr) - 1

    rearranged_arr = []

    # Alternate between picking elements from the beginning and end of the sorted array
    while left <= right:
        if left == right:
            rearranged_arr.append(arr[left])
        else:
            rearranged_arr.append(arr[right])
            rearranged_arr.append(arr[left])
        left += 1
        right -= 1

    return rearranged_arr

# Example usage:
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
result = rearrange_max_min(arr)
print("Rearranged array in maximum and minimum form:", result)
