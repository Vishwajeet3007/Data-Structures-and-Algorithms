def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=' ')
printN(11)
print()
def printNreverse(n):
    if n>0:
        print(n,end=' ')
        printNreverse(n-1)
        
printNreverse(11)
print()
def printNodd(n):
    if n>0:
        printNodd(n-1)
        print(2*n-1,end=' ')
printNodd(11)
print()

def printNoddreverse(n):
    if n>0:
        print(2*n-1,end=' ')
        printNoddreverse(n-1)
        
printNoddreverse(11)
print()
def printNEven(n):
    if n>0:
        printNEven(n-1)
        print(2*n,end=' ')
printNEven(11)
print()
def printNEvenreverse(n):
    if n>0:
        print(2*n,end=' ')
        printNEvenreverse(n-1)
        
printNEvenreverse(11)
