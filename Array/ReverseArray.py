#1.Reversing by slicing
def reverse(arr):
    reversed_arr=arr[::-1]
    return reversed_arr
arr=[1,2,3,4,5]
result=reverse(arr)
print(result)
#2.Reverse using loop
def reverse(arr1):
    reversed_arr=[]
    for i in range(len(arr1)-1,-1,-1):
        reversed_arr.append(arr1[i])
    return reversed_arr
arr1=[1,2,3,4,5,6,7]
result=reverse(arr1)
print(result)

#3.Two pointer approach
def reverse(arr2):
    left,right=0,len(arr2)-1
    while left < right:
        arr2[left] , arr2[right]=arr2[right],arr2[left]
        left +=1
        right -=1
arr2=[1,2,3,4,5,6,7,8,9]
reverse(arr2)
print(arr2)

#4.Using reverse built-in-function
def reverse(arr3):
    arr3.reverse()
    return arr3
        
arr3=[1,2,3,4,5,6,7,8,9,10,11]
result=reverse(arr3)
print(result)