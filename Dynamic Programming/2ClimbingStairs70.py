def ClimbingStairs(n):
    if n <= 3:
        return n
    prev1 = 3
    prev2 = 2
    for _ in range(3,n):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return curr
n = 3
print(ClimbingStairs(n))
n = 2
print(ClimbingStairs(n))
n = 1
print(ClimbingStairs(n))
n = 5
print(ClimbingStairs(n))
