def countTriplets(arr):
    n = len(arr)
    prefix_xor = [0] * (n + 1)
    for i in range(n):
        prefix_xor[i+1] = prefix_xor[i] ^ arr[i]
    triplets = 0
    for i in range(n):
        for k in range(i+1,n+1):
            if prefix_xor[i] == prefix_xor[k]:
                triplets += k - i  - 1
    return triplets
print(countTriplets([2,3,1,6,7]))