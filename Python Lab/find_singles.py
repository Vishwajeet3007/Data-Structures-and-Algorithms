"""
Write a program in python to find the elements that appears once in an arrray
 where every other element appears twice
 """
def find_singles(arr):
    count_dict = {}
    # Count the occurrences of each element in the array
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find elements that appear only once
    singles = []
    for key, value in count_dict.items():
        if value == 1:
            singles.append(key)
    
    return singles

# Example usage:
arr = [4, 3, 2, 4, 1, 3, 2, 1, 8, 9, 9]
result = find_singles(arr)
print("Elements that appear only once:", result)
