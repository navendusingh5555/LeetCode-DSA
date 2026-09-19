# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node):
        if node is None:
            return 0
        
        LH = self.solve(node.left)
        RH = self.solve(node.right)

        if LH == -1 or RH == -1:
            return -1
        
        if abs(LH - RH) > 1:
            return -1

        return 1 + max(LH, RH)

    def isBalanced(self, root: TreeNode | None) -> bool:
        height = self.solve(root)
        if height == -1:
            return False
        return True