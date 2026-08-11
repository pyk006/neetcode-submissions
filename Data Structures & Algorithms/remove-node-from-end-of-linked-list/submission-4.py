# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            head = None
            return head
        size = 0
        current = head
        while current is not None:
            size += 1
            current = current.next
        
        current = head
        to_delete_index = size - n
        if to_delete_index == 0:
            head = head.next
            return head
        for i in range(to_delete_index):
            prev = current
            current = current.next
        prev.next = current.next
        return head
