# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        nodes = defaultdict(lambda : defaultdict(list))
        queue = deque([(root, 0, 0)])
        result = []

        while queue:
            node, col, row = queue.popleft()
            nodes[col][row].append(node.val)

            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))
        
        for col in sorted(nodes.keys()):
            col_vals = []
            for row in sorted(nodes[col].keys()):
                col_vals.extend(sorted(nodes[col][row]))
            result.append(col_vals)
        return result