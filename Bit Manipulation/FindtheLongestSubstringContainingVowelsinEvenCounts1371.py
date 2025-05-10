def findLengthOfLongestSubstring(s):
    # mapp= {"00000":-1}
    # state  = [0] * 5 
    # result = 0

    # for i in range(len(s)):
    #     if s[i] == 'a':
    #         state[0] = (state[0] + 1) % 2
    #     elif s[i] == 'e':
    #         state[1] = (state[1] + 1) % 2
    #     elif s[i] == 'i':
    #         state[2] = (state[2] + 1) % 2
    #     elif s[i] == 'o':
    #         state[3] = (state[3] + 1) % 2
    #     elif s[i] == 'u':
    #         state[3] = (state[3] + 1) % 2
    #     currState = ""
    #     for j in range(5):
    #         currState += str(state[j])
    #     if currState in mapp:
    #         result = max(result,i-mapp[currState])
    #     else:
    #         mapp[currState] = i
    # return result

# using XOR
    mapp= {"00000":-1}
    state  = [0] * 5 
    result = 0

    for i in range(len(s)):
        if s[i] == 'a':
            state[0] = (state[0] ^ 1) 
        elif s[i] == 'e':
            state[1] = (state[1] ^ 1) 
        elif s[i] == 'i':
            state[2] = (state[2] ^ 1) 
        elif s[i] == 'o':
            state[3] = (state[3] ^ 1) 
        elif s[i] == 'u':
            state[3] = (state[3] ^ 1) 
        currState = ""
        for j in range(5):
            currState += str(state[j])
        if currState in mapp:
            result = max(result,i-mapp[currState])
        else:
            mapp[currState] = i
    return result
s = "eleetminicoworoep"
print(findLengthOfLongestSubstring(s))
