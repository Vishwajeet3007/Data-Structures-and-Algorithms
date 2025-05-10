def addTWoArray(arr1,arr2):
    i,j = len(arr1)-1,len(arr2)-1
    result = []
    carry = 0
    while i >= 0 or j >= 0 or carry:
        digit1 = arr1[i] if i >= 0 else 0
        digit2 = arr2[j] if j >= 0 else 0
        total = digit1 + digit2 + carry

        result.append(total % 10)
        carry = total // 10
        i -= 1
        j -= 1
    return "".join(map(str,result[::-1]))
arr1 = [2,4,9]
arr2 = [9,5,8]
print(addTWoArray(arr1,arr2))