def sumOfmultiplesOf3or5(n):
    # result = [num for num in range(n+1) if num % 3 == 0 or num % 5 == 0 ]
    # return sum(result)
    def sumDivisible(x):
        m = n // x
        return x * (m*(m + 1)) // 2
    return sumDivisible(3) + sumDivisible(5) - sumDivisible(15)
n = 10
print(sumOfmultiplesOf3or5(n))