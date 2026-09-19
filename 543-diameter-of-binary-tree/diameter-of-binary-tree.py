# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def calculateHeight(self, node):
        if not node:
            return 0
        
        LH = self.calculateHeight(node.left)
        RH = self.calculateHeight(node.right)
        self.diameter = max(self.diameter, LH + RH)

        return 1 + max(LH, RH)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.calculateHeight(root)
        return self.diameter