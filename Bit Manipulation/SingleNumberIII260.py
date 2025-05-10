from collections import Counter
def singleNumber(nums):
    # using Dictionary
    # freq = Counter(nums)
    # result = [ num for num in freq  if freq[num] == 1]
    # return result

    # Using XOR
    all_xor = 0
    for num in nums:
        all_xor ^= num
    mask = all_xor & (-all_xor)
    groupA = 0
    groupB = 0
    for num in nums:
        if num & mask == 0:
            groupA ^= num
        else:
            groupB ^= num
    return [groupA,groupB]

nums = [1,2,1,3,2,5]
print(singleNumber(nums))
