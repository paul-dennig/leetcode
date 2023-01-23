"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        clones = {node.val: Node(node.val, [])}
        queue = deque([node])

        while queue:
            process_node = queue.popleft()
            current_node = clones[process_node.val]

            for neighbor_node in process_node.neighbors:
                if not (neighbor_node.val in clones):
                    clones[neighbor_node.val] = Node(neighbor_node.val, [])
                    queue.append(neighbor_node)


                current_node.neighbors.append(clones[neighbor_node.val])

        return clones[node.val]
