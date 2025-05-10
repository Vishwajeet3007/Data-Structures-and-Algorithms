def minJumpsToReachEnd(arr):
    n=len(arr)
    maxR=arr[0]
    steps=arr[0]
    jump=1
    if n==1:
        return 0
    elif arr[0]==0:
        return -1
    else:
        for i in range(1,n):
            if i == n-1:
                return jump
            maxR=max(maxR,i+arr[i])
            steps -=1
            if steps == 0:
                jump +=1
                if i >= maxR:
                    return -1
                steps=maxR-i
arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
print(minJumpsToReachEnd(arr))  # Output: 4
            