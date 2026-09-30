# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root, inorder):
        def traverse(node):
            if not node:
                return 
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)
        traverse(root)
        return inorder
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        inorder = []
        self.inorderTraversal(root, inorder)
        return inorder[k - 1]