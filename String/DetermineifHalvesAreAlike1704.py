def halvesAlike(s):
    n = len(s)
    vowels = set('AEIOUaeiou')
    first_half = s[:n//2]
    second_half = s[n//2:]
    count1 = sum(1 for char in first_half if char in vowels)
    count2 = sum(1 for char in second_half if char in vowels)
    return count1 == count2
s = "book"
print(halvesAlike(s))
s = "textbook"
print(halvesAlike(s))