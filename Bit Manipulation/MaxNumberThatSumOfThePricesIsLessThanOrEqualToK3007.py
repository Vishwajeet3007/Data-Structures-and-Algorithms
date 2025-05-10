import math
class  Solution:
    def getBitsCount(self,num):
        if num == 0:
            return []
        bitLen = int(math.log2(num))
        bitsCount = [0] * (bitLen + 1)
        while num > 0:
            bitLen = int(math.log2(num))
            nearpower2 = (1 << bitLen)
            bitsCount[bitLen] += (num-nearpower2 + 1)
            for i in range(bitLen):
                bitsCount[i] += nearpower2 // 2
            num -= nearpower2
        return bitsCount
    
    def findMaximumNumber(self,k,x):
        left = 0
        right = int(1e15)
        result = 0
        while left <=  right:
            mid = left + (right - left ) //  2
            bitsCount = self.getBitsCount(mid)
            totalPrice = 0
            maxLog = len(bitsCount)-1
            for i in range(maxLog+1):
                if (i + 1) % x == 0:
                    totalPrice += bitsCount[i]
            if totalPrice <= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
sol = Solution()
k = 7
x = 2
result = sol.findMaximumNumber(k, x)
print(result)
