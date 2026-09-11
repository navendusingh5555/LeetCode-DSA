# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = deque([])
        queue.append(root)

        while queue:
            level_size = len(queue)
            curr_level = []

            for _ in range(level_size):
                e = queue.popleft()
                curr_level.append(e.val)

                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            result.append(curr_level)
        return result

        