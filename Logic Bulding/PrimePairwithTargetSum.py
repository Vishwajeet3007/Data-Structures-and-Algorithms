import math
class Solution:
    def getPrimes(self,n):
        is_prime = self.sieve(n)
        for prime in range(2,n):
            if is_prime[prime] and is_prime[n-prime]:
                return [prime , n - prime]
        return [-1,-1]
    def sieve(self,limit):
        if limit < 2:
            return [False] * (limit + 1)
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2,int(math.sqrt(limit))+1):
            if is_prime[i]:
                for j in range( i * i , limit + 1 , i):
                    is_prime[j] = False
        return is_prime

n = 10
sol = Solution()
print(sol.getPrimes(n))