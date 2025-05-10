#counting sort
def counting_sort(arr):
    max_element=max(arr)
    count=[0]*(max_element+1)
    for num in arr:
        count[num]+=1
    for i in range(1,len(count)):
        count[i] +=count[i-1]
    #temporary array to store the sorted output
    output = [0]*len(arr)
    
    for num in arr:
        output[count[num] - 1]=num
        count[num]-=1
    return output

#driver code
arr = [2,2,3,4,1,5,1,5,1]
sorted_arr = counting_sort(arr)
print("Sorted array is:", sorted_arr)
