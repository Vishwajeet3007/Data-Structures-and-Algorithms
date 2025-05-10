def numSteps(s):
    steps = 0
    # num = int(s,2)
    # while num > 1:
    #     if num % 2 == 0:
    #         num = num // 2
    #         steps += 1
    #     else:
    #         num += 1
    #         steps += 1
    # return steps

    n = len(s)
    carry = 0
    for i in range(n-1,0,-1):
        if (int(s[i]) + carry ) % 2 == 1:
            steps += 2
            carry = 1
        else:
             steps += 1
    return steps +  carry
print(numSteps("1101"))
print(numSteps("10"))
print(numSteps("1"))

        