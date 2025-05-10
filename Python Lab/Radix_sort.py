def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Initialize the output array
    count = [0] * 10  # Initialize the count array for digits 0 to 9
    
    # Count the occurrences of digits at the specified position (exp)
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Modify the count array to store the actual position of each digit
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array by placing elements in the correct position
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy the sorted elements from the output array to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)  # Find the maximum value in the array
    exp = 1  # Initialize the exponent for the least significant digit
    
    # Iterate through each digit position from least significant to most significant
    while max_val // exp > 0:
        counting_sort(arr, exp)  # Sort the array based on the current digit position
        exp *= 10  # Move to the next digit position

# Example usage
arr = [804,26,5,64,52,1]
print("Original array:", arr)
radix_sort(arr)
print("Sorted array:", arr)
