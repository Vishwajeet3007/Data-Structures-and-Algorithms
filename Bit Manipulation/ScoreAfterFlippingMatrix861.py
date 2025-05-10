def matrixScore(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        if grid[i][0] == 0:
            grid[i] = [ 1 - bit for bit in grid[i]]
    score = 0
    for j in range(n):
        countOnes = sum(grid[i][j] for i in range(m))
        countZeros = m - countOnes
        ones = max(countOnes,countZeros)
        score += (1 << (n-j-1)) * ones
    return score
print(matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
