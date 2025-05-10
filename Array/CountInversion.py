# def countInversion(arr):
#     # Using Brute Force time - O(n^2) and space - O(1)
#     # n=len(arr)
#     # count = 0 
#     # for i in range(n-1):
#     #     for j in range(i+1,n):
#     #         if arr[i] > arr[j]:
#     #             count +=1
#     # return count


'''Using Merge-sort
    Time-complexity - O(nlogn)
    space-complexity - O(1)
    '''
class Solution:
    def __init__(self):
        self.inversion_count = 0  # Use instance variable instead of global

    def inversionCount(self, arr):
        """
        Function to count inversions in the array using Merge Sort.
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        """
        self.inversion_count = 0  # Reset count before sorting
        n = len(arr)
        self.merge_sort(arr, 0, n - 1)
        return self.inversion_count

    def merge(self, arr, start, mid, end):
        """
        Merge function that counts inversions while merging two sorted halves.
        """
        temp = [0] * (end - start + 1)  # Temporary array
        i, j, k = start, mid + 1, 0

        while i <= mid and j <= end:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
                self.inversion_count += (mid - i + 1)  # Count inversions
            k += 1

        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j <= end:
            temp[k] = arr[j]
            j += 1
            k += 1  # Removed extra `k += 1`

        # Copy sorted elements back to the original array
        for i in range(len(temp)):
            arr[start + i] = temp[i]

    def merge_sort(self, arr, start, end):
        """
        Merge Sort function that recursively divides the array.
        """
        if start < end:
            mid = (start + end) // 2
            self.merge_sort(arr, start, mid)
            self.merge_sort(arr, mid + 1, end)
            self.merge(arr, start, mid, end)

# Example Usage
sol = Solution()
arr = [8, 4, 2, 1]
print(sol.inversionCount(arr))  # Output: 6
