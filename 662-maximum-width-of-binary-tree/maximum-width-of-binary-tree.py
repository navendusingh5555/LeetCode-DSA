# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        width = 0
        queue = deque([(root,0)])

        while queue:
            level_size = len(queue)
            _, first_index = queue[0]
            _, last_index = queue[-1]

            width = max(width, last_index - first_index + 1)

            for _ in range(level_size):
                node, index = queue.popleft()
                normalized_index = index - first_index

                if node.left:
                    queue.append((node.left, 2*normalized_index + 1))
                if node.right:
                    queue.append((node.right, 2*normalized_index + 2))
        return width