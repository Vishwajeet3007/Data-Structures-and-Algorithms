class ListNode:
    def __init__(self , val = None , next = None ):
        self.val = val
        self.next = next

class Solution:
    def OddEvenLL(self , head):
        if not head  or  not head.next:
            return head
        oddhead = head
        evenhead = head.next
        evenStart = evenhead
        while evenhead and evenhead.next:
            oddhead.next = oddhead.next.next
            evenhead.next = evenhead.next.next

            oddhead = oddhead.next
            evenhead = evenhead.next

        if oddhead:
            oddhead.next = evenStart
        return head

# Creating nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Creating Linked List: 1 → 2 → 3 → 4 → 5
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Calling function
sol = Solution()
new_head = sol.OddEvenLL(node1)

# Printing output
temp = new_head
while temp:
    print(temp.val, end=" -> " if temp.next else "\n")


    temp = temp.next

