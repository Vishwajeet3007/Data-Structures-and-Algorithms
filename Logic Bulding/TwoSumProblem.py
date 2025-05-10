def TwoSumProblem(arr,target):
    seen = set()
    for num in arr:
        if target-num in seen:
            return True
        seen.add(num)
    return False
arr=[2,3,4,5]
target=9
result = TwoSumProblem(arr,target)
print(result)