class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

def delete_node(node):
    if node is None or node.next is None:
        return
    node.val=node.next.val
    node.next=node.next.next
# Example Usage:
# Creating a linked list: 4 -> 5 -> 1 -> 9
head = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)

head.next = node2
node2.next = node3
node3.next = node4

print("Before deletion:")
temp = head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")

# Delete node with value 5 (we have direct access to it)
delete_node(node2)

print("After deletion:")
temp = head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")

        