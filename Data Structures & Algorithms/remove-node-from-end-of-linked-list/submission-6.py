# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        current = head
        while current is not None:
            current = current.next
            l += 1
        current = head
        prev = None
        if n - l == 0:
            return head.next
        for i in range(l - n):
            prev = current
            current = current.next
        
        prev.next = current.next
        return head