# write  a program of merge sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 # create temp arrays
    L = [0] * n1
    R = [0] * n2
  # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        merge(arr, l, m, r)

arr = [12, 43, 23, 53, 756]
n = len(arr)
print("Given array is:")
for i in range(n):
    print(arr[i], end=" ")

mergeSort(arr, 0, n - 1)

print("\n\nSorted array is:")
for i in range(n):
    print(arr[i], end=" ")
