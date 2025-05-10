class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

def detectCycle(head):
    if head == None:
        return None
    slow = head
    fast = head
    ptr = head

    while head != None and head.next != None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            while slow != ptr:
                slow = slow.next
                ptr = ptr.next
            return slow
    return None

# Creating nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node3  # Creating a cycle here (back to node3)

# Detect cycle
cycle_start = detectCycle(node1)
if cycle_start:
    print(f"Cycle detected at node with value: {cycle_start.val}")
else:
    print("No cycle detected")
