def insertion_sort(list1):
    n=len(list1)
    for i in range(1,n):
        temp=list1[i]
        
        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=temp
mylist=[2,5,1,6,8,3]
insertion_sort(mylist)
print(mylist)