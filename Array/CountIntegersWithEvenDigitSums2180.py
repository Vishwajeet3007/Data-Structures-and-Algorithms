def countIntegers(n):
    count = 0
    for i in range(1,n + 1):
        total = 0
        while i:
            total += i % 10
            i = i // 10
        if total % 2 == 0:
            count += 1
    return count
print(countIntegers(4))
print(countIntegers(30))
