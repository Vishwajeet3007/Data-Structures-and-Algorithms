def Linear_Search(list1):
    x=7
    
    for i in list1:
        if i==x:
            return list1.index(i)
    return None
myList=[2,4,3,7,9,33,66,22]

print(Linear_Search(myList))
print(myList)
    