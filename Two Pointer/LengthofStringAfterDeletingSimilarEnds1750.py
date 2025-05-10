def minimumLength(s):
    left , right = 0 , len(s) - 1
    while left < right and s[left] == s[right]:
        if s[left] != s[right]:
            break
        char = s[left]
        while left <= right and s[left] == char :
            left += 1
        while left <= right and s[right] == char:
            right -= 1
    return right - left + 1
s = "ca"
print(minimumLength(s))
s = "cabaabac"
print(minimumLength(s))
s = "aabccabba"
print(minimumLength(s))