def reverseString(s):
    #return s[::-1]
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
s = 'hello'
print(reverseString(s))