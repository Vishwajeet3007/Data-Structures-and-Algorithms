def FindSum(lst,target):
    n=len(lst)
    for i in range(n):
        for j in range(i+1,n):
            if lst[i]+lst[j]==target:
                return [i,j]
    return []
lst=[3,5,7,9,3,6]
target=13
result=FindSum(lst,target)
print(result)
            
    