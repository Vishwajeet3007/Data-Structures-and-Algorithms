from collections import Counter
def firstUniqueCharacterInString(arr):
    freq  = Counter(arr)
    for i , ch in enumerate(arr):
        if freq[ch] == 1:
            return i
    return -1
# Test cases
print(firstUniqueCharacterInString("leetcode"))      
print(firstUniqueCharacterInString("loveleetcode"))  
print(firstUniqueCharacterInString("aabb"))