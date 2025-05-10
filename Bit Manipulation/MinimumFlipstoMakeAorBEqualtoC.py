def MinimumFlips(a,b,c):
    flips = 0
    while a or b or c:
        if (c & 1) == 1:
            if (a & 1 ) == 0 and (b & 1) == 0:
                flips += 1
        else:
            if (a & 1) == 1:
                flips += 1
            if (b & 1) == 1:
                flips += 1
        a >>= 1
        b >>= 1
        c >>= 1
    return flips
a = 2
b = 6
c = 5
result = MinimumFlips(a,b,c)
print("Minimum flips : ",result)
