# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = float("-inf")

    def helper(self, node):
        if not node:
            return 0
        
        LS = self.helper(node.left)
        RS = self.helper(node.right)

        if LS < 0:
            LS = 0
        if RS < 0:
            RS = 0
        
        self.maxi = max(self.maxi, LS + node.val + RS)

        return node.val + max(LS, RS)

    def maxPathSum(self, root: TreeNode | None) -> int:
        self.helper(root)
        return self.maxi