def kThLargestest(arr,k):
    arr.sort(reverse=True)
    return arr[k-1]
arr=[2,3,45,77896,4,347,6,8,5]
k=2
result=kThLargestest(arr,k)
print("K'th Largest : ",result)