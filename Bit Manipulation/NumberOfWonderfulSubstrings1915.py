from collections import defaultdict
def wonderfulSubStrings(word):
    mp = defaultdict(int)
    mp[0] = 1
    result = 0
    cum_xor = 0
    for ch in word:
        shift = ord(ch) - ord('a')
        cum_xor ^= 1 << shift
        result += mp[cum_xor]
        for i in range(10):
            result += mp[cum_xor ^ (1 << i)]
        mp[cum_xor] += 1
    return result
word = "aba"
print(wonderfulSubStrings(word))