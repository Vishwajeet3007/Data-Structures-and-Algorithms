class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
def removeLLElement(head,val):
    if head==None:
        return None
    dummy=ListNode(0)
    dummy.next=head
    curr=dummy
    while curr.next:
        if curr.next.val==val:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return dummy.next


# Helper function to print the linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Creating a linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

print("Original List:")
print_list(head)

# Removing nodes with value 6
head = removeLLElement(head, 6)

print("\nList after removing 6:")
print_list(head)
