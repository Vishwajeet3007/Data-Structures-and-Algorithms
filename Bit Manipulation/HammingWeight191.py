def NumberOf1Bits(n):
    # method 1
    # return bin(n).count('1')

    # methhod 2
    count = 0
    # while n > 0:
    #     n &= (n-1)
    #     count += 1
    # return count

    #mmethod 3
    while n:
        count += (n % 2)
        n //= 2
    return count

        

print(NumberOf1Bits(11))
