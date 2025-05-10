from collections import Counter

def singleNumber(arr):
    unique = 0
    for num in arr:
        unique ^= num  # XOR operation
    return unique
   
   
   
   
    # freq = Counter(arr)
    # for i in range(len(arr)):
    #     if freq[arr[i]] == 1:
    #         return arr[i]
    
arr =[4, 3, 2, 4, 1, 3, 2] 
result = singleNumber(arr)
print(result)
