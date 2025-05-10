def hasTripletSum(arr,target):
    arr.sort()
    n = len(arr)
    for i in range(n-2):
        j = i + 1
        k = n - 1
        while j < k:
            sum = arr[i] + arr[j] + arr[k]

            if sum == target:
                return True
            if sum < target:
                j += 1
            else:
                k -= 1
    return False
arr = [1,4,7,8,4,2,9]
target = 18
print(hasTripletSum(arr,target)) 