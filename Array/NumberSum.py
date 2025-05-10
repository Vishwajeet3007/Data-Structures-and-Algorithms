def numSum(num):
    result = 0
    for digit in str(num):
        result += int(digit)
    return result
num =  123
print(numSum(num))