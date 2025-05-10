def sort012(arr):
    count0=0
    count1=0
    count2=0

    for i in range(len(arr)):
        if arr[i]==0:
            count0 +=1
        elif arr[i]==1:
            count1 +=1
        elif arr[i]==2:
            count2 +=1
    
    i=0
    while count0 > 0:
        arr[i]=0
        i+=1
        count0 -=1

    while count1 > 0:
        arr[i]=1
        i +=1
        count1 -=1
    
    while count2 > 0:
        arr[i]=2
        i+=1
        count2 -=1
    
    return arr

arr=[1,2,1,0,0,0,1,1,0,1,2]
result=sort012(arr)
print(result)