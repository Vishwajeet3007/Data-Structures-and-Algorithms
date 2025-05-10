def sort(list):
    list.sort()
    set1=set(list)
    dict_count={}
    for i in set1:
        dict_count[i]=list.count(i)
    return dict_count
            
list=[2,3,5,89,5,43,3,2,2,4,6,8,6,8]
result=sort(list)
print("Sorted list:", list)
print("Element counts:", result)