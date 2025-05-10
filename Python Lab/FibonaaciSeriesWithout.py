def fib(n):
    a , b = 0, 1
    while a < n:
        print(a , end=' ')
        a , b = b ,a+ b
    print()
    
#n=int(input("Enter number of terms: "))
fib(5)
