from collections import defaultdict
def maxNumber(arr,k):
    count = 0
    dic = defaultdict(int)
    for num in arr:
        diff = k - num
        if dic[diff] > 0:
            count +=1
            dic[diff] -=1
        else:
            dic[num] +=1
    return count
#Example 1
# nums = [1,2,3,4]
# k = 5

# Example 2
nums = [3,1,3,4,3]
k = 6
print(maxNumber(nums,k))

