class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.curr = None
    
    def recursion(self,head):
        if head == None:
            return True
        
        output = self.recursion(head.next)
        if not output:
            return False
        
        if head.val != self.curr.val:
            return False
        self.curr = self.curr.next
        return output
    
    def isPalindrome(self,head):
        self.curr = head
        return self.recursion(head)
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
values = [1, 2, 2, 1]  # Example 1 (Palindrome)
head = create_linked_list(values)
solution = Solution()
print(solution.isPalindrome(head))  # Output: True

values = [1, 2, 3, 2, 1]  # Example 2 (Palindrome)
head = create_linked_list(values)
print(solution.isPalindrome(head))  # Output: True

values = [1, 2, 3, 4, 2, 1]  # Example 3 (Not a Palindrome)
head = create_linked_list(values)
print(solution.isPalindrome(head)) 