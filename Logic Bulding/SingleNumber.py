from collections import Counter
def FindSingleNumber(arr):
    # using Dictinory
    # freq = Counter(arr)
    # for i in range(len(arr)):
    #     if freq[arr[i]] == 1:
    #         return arr[i]
    # return -1
     
    # Using Xor Method
    single = 0
    for num in arr:
        single ^= num
    return single

arr = [2,6,9,3,2,8,9,6,3]
print(FindSingleNumber(arr)) 
