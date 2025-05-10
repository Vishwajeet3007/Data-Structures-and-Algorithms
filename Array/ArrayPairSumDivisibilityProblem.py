def canPair(arr,k):
    n = len(arr)
    if n % 2 != 0:
        return False
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        found_pairs = False
        for j in range(i+1,n):
            if not visited[j] and (arr[i] + arr[j]) % k == 0:
                visited[i] = True
                visited[j] = True
                found_pairs = True
                break
        if not found_pairs:
            return False
    return True
arr = [9, 5, 7, 3]
k = 6
print(canPair(arr,k))
