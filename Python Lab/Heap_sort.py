def heapify(list1,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    
    if l<n and list1[i] < list1[l]:
        largest=l
    if r<n and list1[largest]<list1[r]:
        largest=r
    if largest!=i:
        list1[i],list1[largest]=list1[largest],list1[i]
        heapify(list1,n,largest)

def heap_sort(list1):
    n=len(list1)
    for i in range(n//2-1,-1,-1):
        heapify(list1,n,i)
    for i in range(n-1,0,-1):
        list1[i],list1[0]=list1[0],list1[i]
        heapify(list1,i,0)
list1 = [12, 11, 13, 5, 6, 7]
heap_sort(list1)
print ("Sorted array is:", list1)
    
    