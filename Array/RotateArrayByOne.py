def rotateArrayByOnePosition(arr):
    # arr[:] = arr[-1:] + arr[:-1]

    a=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=a
    return arr
arr=[1,2,3,4,5,6,7,8,9,0]
result=rotateArrayByOnePosition(arr)
print(result)
