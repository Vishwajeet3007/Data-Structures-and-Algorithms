class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class Solution:
    def addTwoNumber(self,l1,l2):
        dummyNode=ListNode()
        new=dummyNode
        carry=0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            val=v1+v2+carry
            carry=val//10
            val=val%10
            new.next=ListNode(val)
            new=new.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummyNode.next
# Helper function to print the linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Creating first linked list: 2 -> 4 -> 3 (Represents 342)
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Creating second linked list: 5 -> 6 -> 4 (Represents 465)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print("First Number:")
print_list(l1)

print("\nSecond Number:")
print_list(l2)

# Adding the two numbers
sol = Solution()
new_head = sol.addTwoNumber(l1, l2)

print("\nSum of Numbers:")
print_list(new_head)