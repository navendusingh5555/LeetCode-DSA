# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse_preorder(self, node):
        if not node:
            return 
        self.reverse_preorder(node.right)
        self.reverse_preorder(node.left)

        node.right = self.previous
        node.left = None

        self.previous = node

    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.previous = None
        self.reverse_preorder(root)