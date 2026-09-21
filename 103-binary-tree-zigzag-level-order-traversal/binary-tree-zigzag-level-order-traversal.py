# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            curr_level = [0]*level_size

            for i in range(level_size):
                node = queue.popleft()

                index = i if left_to_right else level_size - 1 - i
                curr_level[index] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(curr_level)
            left_to_right = not left_to_right
        return result 