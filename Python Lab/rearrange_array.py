"""
Write a program to rearrange an array such that even position are greater than odd
"""
def rearrange_array(arr):
    # Sort the array in non-decreasing order
    arr.sort()

    # Create lists for even and odd position elements
    even_pos = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    odd_pos = [arr[i] for i in range(len(arr)) if i % 2 != 0]

    # Rearrange the array with even positions greater than odd positions
    rearranged_arr = []
    for i in range(len(even_pos)):
        rearranged_arr.append(even_pos[i])
        if i < len(odd_pos):
            rearranged_arr.append(odd_pos[i])

    return rearranged_arr
arr = [1, 3, 2, 5, 4, 6, 7, 8, 9]
result = rearrange_array(arr)
print("Rearranged array with even positions greater than odd positions:", result)
