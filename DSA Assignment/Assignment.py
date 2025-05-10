def sumN(n):
    if n==1:
        return 1
    return n + sumN(n-1)
print("Sum is",sumN(10))
def sumNodd(n):
    if n==1:
        return 1
    return 2*n-1 + sumNodd(n-1)
print("Sum is",sumNodd(10))
def sumNeven(n):
    if n==1:
        return 2
    return 2*n + sumNeven(n-1)
print("Sum is",sumNeven(10))
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
print("Sum is",fact(5))
def SumNSquare(n):
    if n==1:
        return 1
    return n*n+ SumNSquare(n-1)
print("Sum is",SumNSquare(5))
