def  reverseString(s):
    # Using Two Pointer
    s = s.strip()
    i = j = len(s) - 1
    result = []
    while i >= 0:
        while i >= 0 and s[i] != ' ':
            i -= 1
        result.append(s[i+1:j+1])
        # skip Sapces
        while i >= 0 and s[i] == ' ':
            i -= 1
        j = i
    return  " ".join(result)
    # word = s.split()
    # result = []
    # for i in  range(len(word)-1,-1,-1):
    #     result.append(word[i])
    #     if i != 0:
    #         result.append(" ")
    # return "".join(result)
    
s = "the sky is blue"
print(reverseString(s))
s = "  hello world  "
print(reverseString(s))
s = "a good   example"
print(reverseString(s))
