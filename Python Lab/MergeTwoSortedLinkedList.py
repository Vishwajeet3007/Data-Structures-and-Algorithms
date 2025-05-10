class ListNode:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
def MergeSortedLinkedList(l1,l2):
    dummy=ListNode()
    current=dummy
    while l1 and l2:
        if l1.item < l2.item:
            current.next=l1
            l1=l1.next
        else:
            current.next=l2
            l2=l2.next
        current=current.next
    if l1:
        current.next=l1
    elif l2:
        current.next=l2
    return dummy.next
def Print_Sorted_Ll(node):
    while node:
        print(node.item,end="->")
        node=node.next
    print("None")
l1=ListNode(1,ListNode(5,ListNode(7)))
l2=ListNode(1,ListNode(6,ListNode(8)))
merge_sort=MergeSortedLinkedList(l1,l2)
Print_Sorted_Ll(merge_sort)
