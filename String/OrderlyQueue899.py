def OrderlyQueue(s,k):
    minimum = s
    if k == 1:
        for i in range(len(s)):
            minimum = min(minimum,s[i:] + s[:i])
        return minimum
    else:
        return ''.join(sorted(s))
s = "cba"
k = 1
print(OrderlyQueue(s,k))
s = "baaca"
k = 3
print(OrderlyQueue(s,k))
s = "baaca"
k = 2
print(OrderlyQueue(s,k))

