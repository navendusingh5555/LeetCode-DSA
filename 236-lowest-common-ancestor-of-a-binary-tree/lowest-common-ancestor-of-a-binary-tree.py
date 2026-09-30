# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def solve(self, node, p, q):
        if not node:
            return None
        if node == p or node == q:
            return node
        left = self.solve(node.left, p, q)
        right = self.solve(node.right, p, q)

        if not left and not right:
            return None
        elif not left:
            return right
        elif not right:
            return left
        return node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 
        'TreeNode') -> 'TreeNode':
        return self.solve(root,p,q)