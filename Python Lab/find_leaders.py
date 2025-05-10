
#Write a python program to find leaders in an array.
def find_leaders(arr):
    leaders = []
    max_right = float('-inf')  # Initialize the maximum element encountered from the right
    
    # Iterate through the array from right to left
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max_right:
            leaders.append(arr[i])  # Current element is a leader
            max_right = arr[i]  # Update the maximum element encountered from the right
    
    return leaders[::-1]  # Reverse the leaders list to get the original order

# Example usage:
arr = [16, 1, 4, 3, 5, 1, 12]
result = find_leaders(arr)
print("Leaders in the array:", result)
