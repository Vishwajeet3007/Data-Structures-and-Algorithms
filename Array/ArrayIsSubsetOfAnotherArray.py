def issubset(arr1,arr2):
    for num in arr2:
        if num in arr1:
            continue
        else:
            return False
    return True
arr1 = [3, 1, 2, 2, 1, 5]
arr2 = [1, 2, 1]
print(issubset(arr1,arr2))


from collections import Counter
def isSubset( a, b):
        count1 = Counter(a)
        count2 = Counter(b)
        for num in count2:
            if count2[num] >  count1.get(num,0):
                return False
        return True
arr1 = [3, 1, 2, 2, 3, 5]
arr2 = [1, 2, 1]
print(isSubset(arr1,arr2))

