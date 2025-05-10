def kThSmallest(arr,k):
    arr.sort()
    return arr[k-1]
arr=[2,3,45,77896,4,347,6,8,5]
k=3
result=kThSmallest(arr,k)
print("K'th Smallest : ",result)