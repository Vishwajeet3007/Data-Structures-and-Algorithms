def lengthOfLongestContiguousSubarray(arr):
    prefix_sum = 0
    index_map = { 0 : -1 }
    max_length = 0
    for i in range(len(arr)):
        prefix_sum += 1 if arr[i] == 1 else -1
        if prefix_sum in index_map:
            max_length = max (max_length,i-index_map[prefix_sum])
        else:
            index_map[prefix_sum] = i
    return max_length
    # count = 0
    # result = []
    # for i in range(len(arr)):
    #     if arr[i] == 0:

    #         if arr[i] == 0:

    #             count += 1
    #         elif arr[i] == 1:
    #             count -= 1
    #     elif arr[i] == 1:
    #         if arr[i] == 1:
    #             count += 1
    #         elif arr[i] == 0:
    #             count -= 1
    #     if count != 0:
    #         result.append(arr[i])
    # return len(result)-1
arr = [0, 1, 0, 1, 1, 0, 0]
print(lengthOfLongestContiguousSubarray(arr))
print(lengthOfLongestContiguousSubarray([0, 0, 1, 1, 0]))
print(lengthOfLongestContiguousSubarray([0, 0, 1, 1, 0, 1, 1, 0]))
print(lengthOfLongestContiguousSubarray([0, 1, 0, 1, 1, 0, 0])) 
