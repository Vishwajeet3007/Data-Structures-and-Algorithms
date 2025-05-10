def countPairsWithGivenSum(nums,k):
    count = 0
    dic = {}
    for i in range(len(nums)):
        diff = k - nums[i]
        if diff in dic:
            count += dic[diff]
        if nums[i] in dic:
            dic[nums[i]] += 1
        else:
            dic[nums[i]] = 1
    return count

nums = [1,5,7,1]
k = 6
print(countPairsWithGivenSum(nums,k))