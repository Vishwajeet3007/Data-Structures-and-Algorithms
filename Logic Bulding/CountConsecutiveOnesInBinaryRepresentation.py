def CountOnesInBinaryNumber(num):
    binary_num = format(num,'b')
    #count = binary_num.count('1')
    count = 0
    
    for num in binary_num:
        if num == '1':
            count += 1
    return count
num = 156
result = CountOnesInBinaryNumber(num)
print(result)
