def xorQueries(arr,queries):
    n = len(arr)
    cumXor = [0] * n
    cumXor[0] = arr[0]
    for i in range(1,n):
        cumXor[i] = cumXor[i-1] ^ arr[i]
    result = []
    for l ,r in queries:
        if l == 0:
            result.append(cumXor[r])
        else:
            result.append(cumXor[r] ^ cumXor[l-1])
    return result
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(xorQueries(arr,queries))