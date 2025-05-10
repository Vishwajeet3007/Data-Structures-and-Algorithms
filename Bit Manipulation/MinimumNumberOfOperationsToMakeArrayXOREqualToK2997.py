def minOperation(nums,k):
    totalXOR = 0
    for num in nums:
        totalXOR ^= num
    diff = totalXOR ^ k
    return diff.bit_count()
print(minOperation([2,1,3,4],1))
print(minOperation([2,0,2,0],0))
print(minOperation([2, 3, 5],6))
print(minOperation([4, 7, 9, 2],3))