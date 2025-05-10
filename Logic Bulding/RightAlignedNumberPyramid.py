def patten(n):
    for i in range(1,n+1):
        spaces = " " * (n-i)
        numbers = "" 
        for j in range(1,i+1):
            numbers += str(j) + " "
        print(spaces + numbers.strip())
patten(5)
            