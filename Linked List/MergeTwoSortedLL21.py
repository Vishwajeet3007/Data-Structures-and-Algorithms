class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
def mergeTwoSortedLL(l1,l2):
    # if l1 is None:
    #     return l2
    # if l2 is None:
    #     return l1
    # if l1.val <= l2.val:
    #     l1.next=mergeTwoSortedLL(l1.next,l2)
    #     return l1
    # else:
    #     l2.next=mergeTwoSortedLL(l1,l2.next)
    #     return l2
    # return None    
    
    if not l1:
        return l2
    if not l2:
        return l1
    dummy=ListNode()
    curr =dummy
    while l1 and l2:
        if l1.val<l2.val:
            curr.next=l1
            l1=l1.next
        else:
            curr.next=l2
            l2=l2.next
        curr = curr.next
    if l1:
        curr.next=l1
    else:
        curr.next=l2

    return dummy.next
    
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating two sorted linked lists
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))

print("List 1:")
printList(l1)

print("List 2:")
printList(l2)

# Merging two sorted lists
merged_head = mergeTwoSortedLL(l1, l2)

print("Merged Sorted List:")
printList(merged_head)
