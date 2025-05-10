def singleNoneDuplicate(arr):
    single = 0
    for num in arr:
        single ^= num
    return single
arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
print(singleNoneDuplicate(arr)) 