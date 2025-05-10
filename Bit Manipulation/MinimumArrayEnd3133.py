def minEnd(n,x):
    num = x
    for i in range(1,n):
        num = (num + 1) | x
    return num
n = 2
x = 7
print(minEnd(n,x))
