# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while True:
            if fast==None or fast.next==None or slow ==None: return False
            slow = slow.next
            fast = fast.next.next
            if slow==fast: return True