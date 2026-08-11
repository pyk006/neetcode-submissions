"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        nodeQueue = deque()
        nodeQueue.append(node)
        copy_map = {}
        start = Node(node.val)
        copy_map[node] = start
        while nodeQueue:
            current = nodeQueue.popleft()
            current_copy = copy_map[current]
            for neighbor in current.neighbors:
                if neighbor not in copy_map:
                    nodeQueue.append(neighbor)
                    neighbor_node = Node(neighbor.val)
                    copy_map[neighbor] = neighbor_node
                    current_copy.neighbors.append(neighbor_node)
                else:
                    neighbor_node = copy_map[neighbor]
                    current_copy.neighbors.append(neighbor_node)
            
        return start