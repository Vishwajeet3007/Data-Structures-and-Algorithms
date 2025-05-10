def mergeTwoSortedArray(arr1,arr2,n,m):
    
    i=n-1
    j=m-1
    k=n+m-1
    while j>=0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k]=arr1[i]
            
            i-=1
        else:
            arr1[k]=arr2[j]
            
            j-=1
        k -=1
arr1 = [1, 3, 5, 7] + [0] * 3  # Ensure arr1 has enough space
arr2 = [2, 4, 6]
mergeTwoSortedArray(arr1, arr2, 4, 3)  # Pass correct sizes
print(arr1)