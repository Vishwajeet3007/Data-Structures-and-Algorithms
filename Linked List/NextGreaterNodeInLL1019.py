class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
class Solution:
    def SizeOfLL(self,head):
        count = 0
        curr = head
        while curr:
            count +=1
            curr = curr.next
        return count
    def reverseLL(self,head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def nextGreaterNodeInLL(self,head):
        size = self.SizeOfLL(head)
        arr = [0] * size

        nHead = self.reverseLL(head)
        stack = []
        stack.append(nHead.val)
        curr = nHead.next
        ptr = size - 2
        while ptr >= 0:
            ele = curr.val
            curr = curr.next
            while len(stack) > 0 and stack[-1]<=ele:
                stack.pop()
            if len(stack)==0:
                arr[ptr] = 0
            else:
                arr[ptr]=stack[-1]
            stack.append(ele)
            ptr -=1

        return arr

def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Example Usage
head = createLinkedList([2, 1, 5,6])

sol = Solution()
print(sol.nextGreaterNodeInLL(head))