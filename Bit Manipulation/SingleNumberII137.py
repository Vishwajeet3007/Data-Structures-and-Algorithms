def SingleNumber(arr):
    result = 0
    for k in range(32):
        temp = 1 << k
        countOnes = 0
        for num in arr:
            if (num & temp) != 0:
                countOnes += 1
        if countOnes % 3 != 0:
            result = (result | temp)
    if result >= (1 << 31):
        result -= (1 << 32)
    return result
print(SingleNumber([2,3,2,2,3,5,3]))