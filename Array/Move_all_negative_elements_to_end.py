def Move_all_negative_elements_to_end(arr):
    positive_number=[num for num in arr if num >= 0]
    negative_number=[num for num in arr if num < 0]
    arr[:] =positive_number + negative_number
    return arr
arr=[1,4,6,8,4,-1,5,7,-7,4,6,-9]
result=Move_all_negative_elements_to_end(arr)
print(result)