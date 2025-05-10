class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
class Solution:
    def reverseLL(self,head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr 
            curr = temp
        return prev
# Helper function to print the linked list
def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Creating a linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original Linked List:")
printList(head)

# Creating a Solution object
sol = Solution()

# Reversing the linked list
reversed_head = sol.reverseLL(head)

print("Reversed Linked List:")
printList(reversed_head)