def makeGood(s):
    stack = []
    for char in s:
        if stack and abs(ord(stack[-1]) - ord(char)) == 32:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)
s = "leEeetcode"
print(makeGood(s))
s = "abBAcC"
print(makeGood(s))
s = "s"
print(makeGood(s))