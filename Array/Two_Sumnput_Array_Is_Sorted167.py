def twoSum(arr,target):
    # 0-based indexing
    left = 0
    right =len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left  , right ]
        elif total > target:
            right -= 1
        else:
            left += 1
    return [-1,-1]
arr = [2,7,8,9]
target = 9
print(twoSum(arr,target))