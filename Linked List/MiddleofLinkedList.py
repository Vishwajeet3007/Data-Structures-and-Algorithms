class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next
class Solution:
    def middleOfLL(self,head):
    #     temp = head
    #     count = 0
    #     while temp:
    #         count += 1
    #         temp = temp.next
    #     temp = head
    #     for _ in range(count//2):
    #         temp = temp.next
    #     return temp.val

# Optimal
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val
# Helper function to create linked list from a list
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Create linked list: 1 → 2 → 3 → 4 → 5
head = create_linked_list([1, 2, 3, 4, 5])

# Instantiate Solution and find middle
sol = Solution()
print("Middle of linked list:", sol.middleOfLL(head))
