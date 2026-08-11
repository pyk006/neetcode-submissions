# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        current = head
        while current is not None:
            leng += 1
            current = current.next
        
        if leng == n:
            return head.next
        prev = None
        current = head
        for i in range(leng - n):
            prev = current
            current = current.next
        
        prev.next = current.next
        return head
        