# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        if not root:
            return 0

        parent_track = {}
        start_node = None

        queue = deque([root])
        parent_track[root] = None

        while queue:
            node = queue.popleft()
            if node.val == start:
                start_node = node
            if node.left:
                parent_track[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_track[node.right] = node
                queue.append(node.right)
        
        queue = deque([start_node])
        infected = {start_node}
        time = 0

        while queue:
            level_size = len(queue)
            spread = False

            for _ in range(level_size):
                node = queue.popleft()
                if node.left and node.left not in infected:
                    infected.add(node.left)
                    queue.append(node.left)
                    spread = True

                if node.right and node.right not in infected:
                    infected.add(node.right)
                    queue.append(node.right)
                    spread = True
                
                parent = parent_track[node]
                if parent and parent not in infected:
                    infected.add(parent)
                    queue.append(parent)
                    spread = True
            if spread:
                time += 1
        return time