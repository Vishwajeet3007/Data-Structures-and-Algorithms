def countOddEven(arr):
    even_count = sum(1 for num in arr if num%2==0)
    odd_count = len(arr)-even_count
    return [odd_count,even_count]
arr=[1,2,3,4,5]
result = countOddEven(arr)
print(result)