def kthElementInSortedMatrix(matrix,k):
    #T.C= O(N² log N²) 
    # flat_nums = [ num for row in matrix for num in row]
    # flat_nums.sort()
    # return flat_nums[k-1]

    n = len(matrix)
    low, high = matrix[0][0], matrix[n-1][n-1]
    def count_less_equal(matrix, mid):
        j = n - 1
        count = 0
        for i in range(n):
            while j >= 0 and matrix[i][j] > mid:
                j -= 1
            count += j + 1
        return count
    while low < high:
        mid = (low + high) // 2
        if count_less_equal(matrix, mid) < k:
            low = mid + 1  # Move right if count is less than k
        else:
            high = mid  # Narrow down the search

    return low


    # T.C = (O(N log M))
print(kthElementInSortedMatrix([
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]  
,8))