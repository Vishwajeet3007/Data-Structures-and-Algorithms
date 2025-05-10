def minDeletionSize(strs):
    count = 0
    for col in range(len(strs[0])):
        for row in range(1,len(strs)):
            if strs[row][col] < strs[row-1][col]:
                count += 1
                break
    return count
strs = ["cba","daf","ghi"]
print(minDeletionSize(strs))
strs = ["a","b"]
print(minDeletionSize(strs))
strs = ["zyx","wvu","tsr"]
print(minDeletionSize(strs))