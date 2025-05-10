def KthMax(list1,n,k):
    list1.sort(reverse=True)
    return list1[k-1]
def KthMin(list1,n,k):
    list1.sort()
    return list1[k-1]
list1=[345,56,7,4,2,5,46]
n=len(list1)
k=2
print("K'th Maximum element:",KthMax(list1,n,k))
print("K'th Minimum element:",KthMin(list1,n,k))
    
    