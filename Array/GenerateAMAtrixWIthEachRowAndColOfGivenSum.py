from typing import List

class Solution:
    def generateMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        matrix = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                matrix[i][j] = min(rowSum[i],colSum[j])
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix
    
sol = Solution()

print(sol.generateMatrix([3, 8], [4, 7])) 
# Output: [[3, 0], [1, 7]]

print(sol.generateMatrix([5, 7, 10], [8, 6, 8]))
# Output: [[5, 0, 0], [3, 4, 0], [0, 2, 8]]

print(sol.generateMatrix([2, 2], [1, 1, 2])) 
# Output: [[1, 1, 0], [0, 0, 2]]



        # n, m = len(rowSum), len(colSum)
        # matrix = [[0] * m for _ in range(n)]

        # for i in range(n):
        #     for j in range(m):
        #         matrix[i][j] = min(rowSum[i], colSum[j])  # Assign the minimum possible value
        #         rowSum[i] -= matrix[i][j]  # Reduce the row sum
        #         colSum[j] -= matrix[i][j]  # Reduce the column sum

        # return matrix