#Write a  program in python to reverse an array.
def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
     arr[start], arr[end] = arr[end] , arr[start]
     start +=1
     end -=1
arr = input("Enter the elements of the array seperated by spaace:").split()
arr = [int(x) for x in arr]
print("Original arrays: ",arr)
reverse_array(arr)
print("Reversed arrays: " , arr)