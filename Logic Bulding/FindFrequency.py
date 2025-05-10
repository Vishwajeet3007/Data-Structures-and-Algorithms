from collections import Counter
def findFreqency(arr):
    
    #freq = Counter(arr)
    freq = {}
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
    return freq 

arr=[2,6,3,2,7,4,3,5,2]
result = findFreqency(arr)
print(result)