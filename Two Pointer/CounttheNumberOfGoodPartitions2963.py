def numberOfGoodPartitions(nums):
    mod = 10 ** 9 + 7
    last_index = {num : i for i, num in enumerate(nums)}
    count = 0
    end = 0
    for i , num in enumerate(nums):
        end = max(end,last_index[num])
        if i == end :
            count += 1
    return pow(2,count - 1,mod)
nums = [1,1,1,1]
print(numberOfGoodPartitions(nums))
nums = [1,2,1,3]
print(numberOfGoodPartitions(nums))
nums = [1,2,3,4]
print(numberOfGoodPartitions(nums))