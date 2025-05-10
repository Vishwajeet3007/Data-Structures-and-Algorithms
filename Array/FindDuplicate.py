def findDuplicates(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            return arr[i]
    return -1
arr=[1,2,3,4,5,2]
print(findDuplicates(arr))