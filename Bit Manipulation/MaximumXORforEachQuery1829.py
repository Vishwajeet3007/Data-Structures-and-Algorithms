def maximumXOR(nums,maximumBit):
    max_value = (1 << maximumBit) - 1
    prefix_xor = 0
    result = []
    for num in nums:
        prefix_xor ^= num
        result.append(prefix_xor ^ max_value)
    return result[::-1]
nums = [0,1,1,3]
maximumBit = 2
print(maximumXOR(nums,maximumBit))