def sumOfMaxMin(arr):
    n=len(arr)
    maxx=minn=arr[0]
    for i in range(1,n):
        if arr[i]>maxx:
            maxx=arr[i]
        elif arr[i]<minn:
            minn=arr[i]
    return maxx + minn
arr=[1,3,6,8,43,6,6]
result=sumOfMaxMin(arr)
print(result)