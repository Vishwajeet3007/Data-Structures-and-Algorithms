from collections import Counter
def isContainsDuplicateNumber(arr):
    freq = Counter(arr)
    for ch in freq:
        if freq[ch] > 1:
            return True
    return False
print(isContainsDuplicateNumber([1,2,3,1]))
print(isContainsDuplicateNumber([1,2,3,4]  ))
print(isContainsDuplicateNumber([1,1,1,3,3,4,2,4,2]))
