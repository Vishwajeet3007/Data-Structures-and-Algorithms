import sys

def matrix_chain_order(p):
    """
    Function to find the most efficient way to multiply the given sequence of matrices
    p: List of dimensions such that matrix Ai has dimensions p[i-1] x p[i]
    """
    # Number of matrices
    n = len(p) - 1
    
    # m[i][j] will hold the minimum number of scalar multiplications needed to compute the matrix A[i]A[i+1]...A[j] = A[i..j]
    m = [[0 for x in range(n)] for y in range(n)]
    
    # s[i][j] will hold the index at which the optimal split occurs
    s = [[0 for x in range(n)] for y in range(n)]

    # l is chain length
    for l in range(2, n+1): # l is the chain length
        for i in range(n-l+1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    """
    Function to print the optimal parenthesization of the matrix chain product
    s: The 2D list storing the optimal split points
    i: Starting index of the matrix chain
    j: Ending index of the matrix chain
    """
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

# Example usage
if __name__ == "__main__":
    # Example dimensions: p = [30, 35, 15, 5, 10, 20, 25]
    p = [30, 35, 15, 5, 10, 20, 25]
    
    m, s = matrix_chain_order(p)
    
    print("Minimum number of multiplications is:", m[0][len(p) - 2])
    
    print("Optimal parenthesization is: ", end="")
    print_optimal_parens(s, 0, len(p) - 2)
    print()