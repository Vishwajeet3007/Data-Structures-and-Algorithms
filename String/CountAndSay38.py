def countAndSay(n):
    if n == 1:
        return '1'
    say = countAndSay(n-1)
    result = ""
    i = 0
    while i < len(say):
        count = 1
        while i + 1 < len(say) and say[i] == say[i+1]:
            count += 1
            i += 1
        result += str(count) + say[i]
        i += 1
    return result
n = 5
print(countAndSay(n))
n = 4
print(countAndSay(n))
n = 1
print(countAndSay(n))
n = 7 
print(countAndSay(n))
n = 9
print(countAndSay(n))