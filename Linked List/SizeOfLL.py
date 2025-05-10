class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
class Solution:
    def sizeOfLL(self,head):
        count = 0
        curr = head
        while curr:
            count +=1
            curr = curr.next
        return count
# Creating a linked list: 10 -> 20 -> 30 -> 40 -> None
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)

# Creating a Solution object
sol = Solution()

# Getting the size of the linked list
print(sol.sizeOfLL(head))