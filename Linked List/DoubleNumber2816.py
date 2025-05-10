class ListNode:
    def __init__(self,val = None,next = None):
        self.val=val
        self.next=next
class Solution:
    def doubleNumber(self,head):
        def reverse(head):
            curr=head
            prev=None
            while curr!=None:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        nhead = reverse(head)
        dummy=ListNode(-1)
        carry = 0
        ans=dummy
        while nhead:
            summ=nhead.val+nhead.val+carry
            s=summ%10
            carry=summ//10
            temp=ListNode(s)
            dummy.next=temp
            dummy=temp
            nhead=nhead.next
        if carry>0:
            temp=ListNode(carry)
            dummy.next=temp
        ans=reverse(ans.next)
        return ans
# Helper function to print the linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Creating a linked list: 1 -> 2 -> 3 (which represents the number 123)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

print("Original List:")
print_list(head)

# Doubling the number
sol = Solution()
new_head = sol.doubleNumber(head)

print("\nDoubled Number List:")
print_list(new_head)
