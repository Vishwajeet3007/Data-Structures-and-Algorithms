class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class Solution:
    # Merge Two Sorted LL
    def mergeTwoSortedLL(self,l1,l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoSortedLL(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoSortedLL(l1,l2.next)
            return l2
        return None
    
    
    def partitionAndMerge(self,start,end,lists):
        if start > end:
            return None
        if start == end:
            return lists[start]
        mid = start + (end-start) // 2
        l1 = self.partitionAndMerge(start,mid,lists)
        l2 = self.partitionAndMerge(mid + 1,end,lists)
        return self.mergeTwoSortedLL(l1,l2)
    
    def mergeKLists(self,lists):
        k = len(lists)
        if k == 0:
            return None
        return self.partitionAndMerge(0,k-1,lists)

# Helper function to create a linked list from a list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating k sorted linked lists
lists = [
    createLinkedList([1, 4, 5]),
    createLinkedList([1, 3, 4]),
    createLinkedList([2, 6])
]

# Creating Solution object and merging k lists
sol = Solution()
merged_head = sol.mergeKLists(lists)

# Printing the merged linked list
printLinkedList(merged_head)

