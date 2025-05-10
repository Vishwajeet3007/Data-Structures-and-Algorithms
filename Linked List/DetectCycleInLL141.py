class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def hasCycle(head):
    if head==None or head.next==None:
        return False
    slow=head
    fast=head

    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

# Example Usage:
# Creating a cycle for testing
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head.next  # Creates a cycle

print(hasCycle(head))

# Test case without a cycle
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)

print(hasCycle(head2)) 