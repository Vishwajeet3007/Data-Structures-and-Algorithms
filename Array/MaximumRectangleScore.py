def maxRectangleScore(grid):
    
    n, m = len(grid), len(grid[0])
    max_score = 0
    heights = [0] * m  # Rolling array to track consecutive valid column heights

    # Iterate through each row as the "top" boundary
    for top in range(n):
        for col in range(m):
            if top == 0 or grid[top][col] == grid[top - 1][col]:  
                heights[col] += 1  # Increase height if same value continues
            else:
                heights[col] = 1  # Reset height for new top boundary

        # Use a monotonic stack to find max valid rectangle width
        stack = []
        for col in range(m + 1):  # Extra iteration for stack cleanup
            while stack and (col == m or heights[col] < heights[stack[-1]]):
                h = heights[stack.pop()]
                w = col if not stack else col - stack[-1] - 1
                if h >= 2 and w >= 2:
                    max_score = max(max_score, grid[top][col - 1])  # Store highest value
            stack.append(col)

    return max_score

# Example test cases
grid1 = [[1, 2, 2, 2], 
         [2, 2, 2, 2], 
         [3, 4, 2, 8]]

grid2 = [[5, 5, 5], 
         [5, 5, 6], 
         [5, 5, 5]]

grid3 = [[7, 7]]

print(maxRectangleScore(grid1))  # Output: 2
print(maxRectangleScore(grid2))  # Output: 5
print(maxRectangleScore(grid3))  # Output: 0



#     n, m = len(grid), len(grid[0])
#     max_score = 0

#     # Iterate through all possible top-left corners
#     for i in range(n):
#         for j in range(m):
#             value = grid[i][j]

#             # Expand rectangle downwards
#             for h in range(2, n - i + 1):  
#                 if any(grid[i + h - 1][j] != value for j in range(m)):  # Check row consistency
#                     break

#                 # Expand rectangle rightwards while keeping it valid
#                 for w in range(2, m - j + 1):
#                     if any(grid[row][j + w - 1] != value for row in range(i, i + h)):  # Check column consistency
#                         break
                    
#                     # Valid rectangle found, update max_score
#                     max_score = max(max_score, value)
    
#     return max_score

# # Example test cases
# grid1 = [[1, 2, 2, 2], 
#          [2, 2, 2, 2], 
#          [3, 4, 2, 8]]

# grid2 = [[5, 5, 5], 
#          [5, 5, 6], 
#          [5, 5, 5]]

# grid3 = [[7, 7]]

# print(maxRectangleScore(grid1))  # Output: 2
# print(maxRectangleScore(grid2))  # Output: 5
# print(maxRectangleScore(grid3))  # Output: 0