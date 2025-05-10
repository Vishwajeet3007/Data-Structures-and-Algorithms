class Solution:
    def getMinDiff(self, arr,k):
        arr.sort()
        n=len(arr)
        smallest=arr[0]+k
        largest=arr[n-1]-k
        diff=arr[n-1]-arr[0]
        
        for i in range(1,n):
            if arr[i]-k < 0:
                continue
            mini = min(smallest,arr[i]-k)
            maxx = max(largest,arr[i-1]+k)
            diff=min(diff,maxx-mini)
        return diff
arr = [1, 5, 8, 10]
k = 2
sol = Solution()
print(sol.getMinDiff(arr, k))
