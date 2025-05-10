def digitalRoot(arr):
    summ = sum(arr)
    num = list(map(int, str(summ)))
    while len(num) > 1:

        summ = sum(num)
        num = list(map(int, str(summ)))

    return summ
arr = [9,8,7,5,3]
result = digitalRoot(arr)
print(result)