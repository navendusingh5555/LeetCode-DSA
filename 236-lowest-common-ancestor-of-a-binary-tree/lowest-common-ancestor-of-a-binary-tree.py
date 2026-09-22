# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPath(self, node, target, path):
        if not node:
            return None
        path.append(node)
        if node is target:
            return True
        if self.findPath(node.left, target, path) or self.findPath(node.right, target, path):
            return True
        path.pop()
        return False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = []
        path_q = []

        self.findPath(root, p, path_p)
        self.findPath(root, q, path_q)

        limit = min(len(path_p), len(path_q))
        lca = None

        for i in range(limit):
            if path_p[i] is not path_q[i]:
                break
            lca = path_p[i]
        return lca