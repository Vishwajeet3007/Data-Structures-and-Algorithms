def findPeak(list1,n):
  if n==1:
    return [0]
  list2=[]
  if list1[0]>=list1[1]:
    list2.append(0)
  if list1[n-1]>=list1[n-2]:
    list2.append(n-1)
  for i in range(1,n-1):
    if list1[i]>=list1[i-1] and list1[i]>=list1[i+1]:
      list2.append(i)
  return list2
list1=[5,10,8,20,15]
n=len(list1)
print(findPeak(list1,n))