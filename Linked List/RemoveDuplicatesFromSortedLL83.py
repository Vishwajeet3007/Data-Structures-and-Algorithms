class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
def removeDuplicates(head):
    if not head:
        return head
    curr = head
    while curr.next:
        if curr.val==curr.next.val:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return head
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating a sorted linked list: 1 -> 1 -> 2 -> 3 -> 3 -> 4
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4))))))

print("Original List:")
printList(head)

# Removing duplicates
head = removeDuplicates(head)

print("List after removing duplicates:")
printList(head)
