#To find the number of occurence in an array
def find_occurrences(arr):
    arr.sort()
    i = 0
    while i < len(arr):
        count = 1  # Initialize count for each element
        if i < len(arr) - 1 and arr[i] == arr[i + 1]:
            # Use binary search to find the last occurrence of the current element
            last_index = binary_search_last_index(arr, arr[i])
            count = last_index - i + 1  # Calculate count
            i = last_index  # Move the pointer to the last occurrence
        print("Element", arr[i], "occurs", count, "times.")
        i += 1

def binary_search_last_index(arr, target):
    low = 0
    high = len(arr) - 1
    last_index = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last_index = mid
            low = mid + 1  # Continue searching in the right half
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last_index

# Get user input for the array
arr = input("Enter the elements of the array separated by space: ").split()
arr = [int(x) for x in arr]  # Convert input strings to integers

find_occurrences(arr)
