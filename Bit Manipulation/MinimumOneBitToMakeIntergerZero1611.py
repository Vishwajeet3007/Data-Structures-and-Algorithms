def minimumOneBitOperation(n):
    result = 0
    while n:
        result ^= n
        n >>= 1
    return result
    
print(minimumOneBitOperation(9))