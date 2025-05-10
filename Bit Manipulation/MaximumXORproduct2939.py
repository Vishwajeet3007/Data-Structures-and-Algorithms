def maximumXORProduct(a,b,n):
    xXora = 0
    xXorb = 0
    m = int(1e9 + 7)
    # from 49 to n-1 bit
    for i in range(49,n-1,-1):
        a_ith_bit = ((a >> i) & 1)
        b_ith_bit = ((b >> i) & 1)
        if a_ith_bit == 1:
            xXora ^= (1 << i)
        if b_ith_bit == 1:
            xXorb ^= (1 << i)
    
    # from n-1 to 0 bits
    for i in range(n-1,-1,-1):
        a_ith_bit = ((a >> i) & 1)
        b_ith_bit = ((b >> i) & 1)

        if a_ith_bit == b_ith_bit:
            xXora ^= (1 << i)
            xXorb ^= (1 << i)
        elif xXora > xXorb:
            xXorb ^= (1 << i)
        else:
            xXora ^= (1 << i)
    xXora %= m
    xXorb %= m
    return (xXora * xXorb) % m
a = 12
b = 5
n = 4
print(maximumXORProduct(a,b,n))

        