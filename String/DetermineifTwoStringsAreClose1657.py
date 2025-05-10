def closeStrings(word1,word2):
    if len(word1) != len(word2):
        return False
    freq1 = [0] * 26
    freq2 = [0] * 26
    for ch in word1:
        freq1[ord(ch) - ord('a')] += 1
    for ch in word2:
        freq2[ord(ch) - ord('a')] += 1
    for i in range(26):
        if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
            return False
    return sorted(freq1) == sorted(freq2)
print(closeStrings("abc", "bca"))         
print(closeStrings("a", "aa"))            
print(closeStrings("cabbba", "abbccc"))   
print(closeStrings("cabbba", "aabbss")) 