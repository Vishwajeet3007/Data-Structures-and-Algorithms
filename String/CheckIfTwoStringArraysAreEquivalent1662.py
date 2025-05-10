def arrayStringAreEqual(word1,word2):
    #return "".join(word1) == "".join(word2)
    i = j = 0
    p1 = p2 = 0
    while i < len(word1) and j < len(word2):
        if word1[i][p1] != word2[j][p2]:
            return False
        p1 += 1
        p2 += 1

        if p1 == len(word1[i]):
            p1 = 0
            i += 1
        if p2 == len(word2[j]):
            p2 = 0
            j += 1
    return i == len(word1) and j == len(word2)
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arrayStringAreEqual(word1,word2))
word1 = ["a", "cb"]
word2 = ["ab", "c"]
print(arrayStringAreEqual(word1,word2))
word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
print(arrayStringAreEqual(word1,word2))