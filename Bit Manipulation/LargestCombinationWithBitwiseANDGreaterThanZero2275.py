def largestCombination(candidates):
    count = [0] * 32
    result = 0
    for i in range(32):
        for num in candidates:
            if num & (1 << i) != 0:
                count[i] += 1
        result = max(result,count[i])
    return result
candidates = [16,17,71,62,12,24,14]
print(largestCombination(candidates))