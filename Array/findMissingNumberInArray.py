def missing_number(arr):
   #from 1 to n
    n=len(arr)+1
    # # from 0 to n
    # n=len(arr)
    total_sum=n*(n+1)//2
    actual_sum=sum(arr)
    return total_sum-actual_sum
arr=[1,2,4,5,6,7]
result=missing_number(arr)
print(result)