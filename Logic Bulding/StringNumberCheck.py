def fac(x):
    if x == 0 or x == 1:
        return 1
    else:
       return x *  fac(x - 1)
def isStrongNumber(n):
    sum_of_fac = sum(fac(int(digit)) for digit in str(n))
    return n == sum_of_fac
    

print(isStrongNumber(145))

print(isStrongNumber(123))
        
        