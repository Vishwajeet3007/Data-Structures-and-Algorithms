def Binary_Search(list1,l,r,item):
    list1.sort()
    if l>r:
        return None
    mid=(l+r)//2
    if item==list1[mid]:
        return mid
    if item<list1[mid]:
        return Binary_Search(list1,l,mid-1,item)
    else:
        return Binary_Search(list1,mid+1,r,item)

item=int(input("Enter the item you want to search:"))
mylist1=[2,4,3,7,9,33,66,22]

index=Binary_Search(mylist1,0,len(mylist1)-1,item)
if index==None:
    print("Item not found.")
else:
    print("Item ",item,"found at index ",index)