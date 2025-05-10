class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
def deleteMiddle(head):
    if not head or not head.next:
        return None
    slow=head
    fast=head
    pre=slow

    while fast and fast.next:
        pre = slow
        fast=fast.next.next
        slow=slow.next
    pre.next=pre.next.next
    return head
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,ListNode(6))))))

print("Original List:")
printList(head)

# Deleting middle node
head = deleteMiddle(head)

print("List after deleting middle:")
printList(head)
