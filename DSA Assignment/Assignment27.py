def quick_sort(l):
    if len(l)<=1:
        return l
    else:
        pivot=l[0]
        lesser=[x for x in l[1:] if x<=pivot]
        greater=[x for x in l[1:] if x>pivot]
        return quick_sort(lesser) + [pivot]+quick_sort(greater) 
mylist=[53,11,72,68,41,25,18,37,44,80]
mylist=quick_sort(mylist)
print(mylist)
        