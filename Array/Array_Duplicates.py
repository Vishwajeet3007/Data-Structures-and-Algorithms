from collections import Counter
def array_duplicates(arr):
    freq = Counter(arr)
    return [key for key , value in freq.items() if value  > 1]
arr=[2,3,5,7,4,5,2,3,4,6,2,44,3]
result=array_duplicates(arr)
print(result)

# def array_duplicates(arr):
#     seen = set()
#     result = []

#     for num in arr:
#         if num in seen:  # If already seen, it's a duplicate
#             result.append(num)
#         else:
#             seen.add(num)  # Add to the set

#     return result
# arr=[2,3,5,7,4,5,2]
# result=array_duplicates(arr)
# print(result)