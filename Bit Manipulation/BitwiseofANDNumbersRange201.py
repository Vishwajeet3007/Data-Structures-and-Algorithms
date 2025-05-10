def rangeBitwiseAnd(left,right):
    # First method
    # shiftcount =0 
    # while left != right:
    #     left = left >> 1
    #     right = right >> 1
    #     shiftcount += 1
    # return left << shiftcount
  # second method
  
    while left < right :
        right = right & (right - 1)
    return right 
print(rangeBitwiseAnd(5, 7))
