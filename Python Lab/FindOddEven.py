
def FindEvenOdd(n):
    even = []
    odd = []
    for i in range(n):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

n = 10
even_result, odd_result = FindEvenOdd(n)
print(f"Even numbers: {even_result}")
print(f"Odd numbers: {odd_result}")
