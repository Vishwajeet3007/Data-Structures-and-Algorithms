def unionOfTwoArray(arr1,arr2):

    # result = set(arr1 + arr2)
    # return result

    # arr1=set(arr1)
    # arr2=set(arr2)
    # result=arr1.union(arr2)
    # return result

    result = set()
    for i in range(len(arr1)):
        result.add(arr1[i])
    for i in range(len(arr2)):
        result.add(arr2[i])
    return result
    



arr1=[1,2,3]
arr2=[3,5,4,5]
result=unionOfTwoArray(arr1,arr2)
print(result)