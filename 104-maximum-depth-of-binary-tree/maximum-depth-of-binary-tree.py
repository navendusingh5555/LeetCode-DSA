# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([])
        queue.append(root)
        height = 0

        while queue:
            level_size = len(queue)
            height += 1

            for _ in range(level_size):
                e = queue.popleft()
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
        return height