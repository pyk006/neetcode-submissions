"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copi = Node(0)
        copi_head = copi
        current = head
        node_dict = {}
        while current is not None:
            copi_head.next = Node(current.val)
            node_dict[current] = copi_head.next
            copi_head = copi_head.next
            current = current.next
        copi_head = copi.next
        current = head
        while current is not None:
            if current.random is None:
                copi_head.random = None
            else:
                copi_head.random = node_dict[current.random]
            current = current.next
            copi_head = copi_head.next
        return copi.next