def ConvertNumberToBinary(num):
    #binary_num = format(num,'b')
    binary_num = bin(num)[2:]
    return binary_num
num = 156
result = ConvertNumberToBinary(num)
print(result)