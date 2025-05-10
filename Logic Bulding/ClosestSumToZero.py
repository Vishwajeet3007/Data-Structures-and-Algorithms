def closestSumToZero(arr):
    # #Method 1
    # closestSTZ = []
    # for i in range(len(arr)-1):
    #     for j in range(1,len(arr)):
    #         closestSTZ.append(arr[i] + arr[j])
    # closestSTZ.sort()
    # for i in range(len(closestSTZ)):
    #     if closestSTZ[i] > 0:
    #         return closestSTZ[i]

    # Method 2
    arr.sort()
    left , right = 0 , len(arr) - 1
    closest_sum = float('inf')
    pairs_sum = (arr[left],arr[right])
    while left < right:
        current_sum = arr[left] + arr[right]
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            pairs_sum = (arr[left],arr[right])
        if current_sum < 0:
            left += 1
        else:
            right -= 1
    return pairs_sum
arr = [10, 20, -30, -5, 6]
print(closestSumToZero(arr))


