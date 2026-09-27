# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:

    def build_parent_track(self, root, parent_track):
        queue = deque([root])
        parent_track[root] = None

        while queue:
            node = queue.popleft()
            if node.left:
                parent_track[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_track[node.right] = node
                queue.append(node.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        parent_track = {}
        self.build_parent_track(root, parent_track)
        queue = deque([target])
        visited = {target}
        dist = 0

        while queue:
            if dist == k:
                break
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                parent = parent_track[node]
                if parent and parent not in visited:
                    visited.add(parent)
                    queue.append(parent)
            dist += 1
        return [node.val for node in queue]