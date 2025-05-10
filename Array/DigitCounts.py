def evenlyDivides(n):
    count = 0
    for i in str(n):
        digit = int(i)
        if digit != 0 and n % digit == 0:
            count += 1
    return count
print(evenlyDivides(1012))  # Output: 3 (since 1012 is divisible by 1, 1, and 2)
print(evenlyDivides(120)) 