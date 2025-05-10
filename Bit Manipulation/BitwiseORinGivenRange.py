def bitwiseOrInGivenRange(left,right):
    # first method

    if left == right:
        return left
    # mask = left ^ right
    # msb =  1 << mask.bit_length()
    # return right | (msb - 1)

    # second method
    while left < right :
        left |= right
        right |= right - 1
    return right 

print(bitwiseOrInGivenRange(3,8))