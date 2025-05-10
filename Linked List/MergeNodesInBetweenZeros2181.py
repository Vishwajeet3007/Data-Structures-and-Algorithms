class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
def mergeNodesInBetweenZeros(head):
    dummy = ListNode(-1)
    ans = dummy
    curr = head.next
    summ = 0

    while curr:
        if curr.val != 0:
            summ += curr.val
        else:
            temp = ListNode(summ)
            ans.next = temp
            ans = ans.next
            summ = 0
        curr = curr.next
    return dummy.next

# Helper function to create a linked list from a list
def createLinkedList(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next  # Returning dummy, so head is at dummy.next

# Helper function to print the linked list
def printLinkedList(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" → ".join(result))

# Example input
arr = [0, 3, 1, 0, 4, 5, 2, 0, 1, 0]
head = createLinkedList(arr)

# Merge nodes
new_head = mergeNodesInBetweenZeros(head)

# Print the merged linked list
printLinkedList(new_head)
