def findAnswer(N, A):
    result = [0] * N
    left = 0
    curr_sum = 0
    for i in range(N):
        curr_sum = 0
        for right in range(i,N):
            curr_sum += A[right]
            if curr_sum > 0:
                result[i] = right - i + 1
                break
    return result
# Example test cases
print(findAnswer(3, [-4, 3, 4]))  # Output: [3, 1, 1]
print(findAnswer(5, [-2, -3, 5, -2, 1]))  # Output: [0, 2, 1, 0, 1]
