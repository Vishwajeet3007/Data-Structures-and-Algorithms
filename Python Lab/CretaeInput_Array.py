import numpy as np 
l=[]
n=int(input("Enter the number: "))
for i in range(1,n):
    term=int(input("Enter the {} term: ".format(i)))
    l.append(term)
print(np.array(l))