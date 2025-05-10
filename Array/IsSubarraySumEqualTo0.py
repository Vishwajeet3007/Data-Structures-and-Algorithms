def isSubArraySumZero(arr):
    sett = set()
    summ = 0
    for i in range(len(arr)):
        summ += arr[i]
        if summ == 0 or summ in sett:
            return True
        sett.add(summ)
    return False
arr = [4, 2, -3, 1, 6]
print(isSubArraySumZero(arr)) 