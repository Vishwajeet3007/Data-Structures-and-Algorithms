def MaxMin(list1):
  max=min=list1[0]
  for num in list1[1:]:
    if num<min:
      min=num
    elif num>max:
      max=num
  return [max,min]
list1=[1,2,3,4,5,6,7,8,9,10]
result=MaxMin(list1)
print(f"Maximum element in given list is {result[0]}")
print(f"Minimum element in given list is {result[1]}")