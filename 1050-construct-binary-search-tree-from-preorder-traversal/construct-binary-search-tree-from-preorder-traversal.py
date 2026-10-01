# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert_node(self, root, value):
        if root is None:
            return TreeNode(value)
        if root.val > value:
            root.left = self.insert_node(root.left, value)
        elif root.val < value:
            root.right = self.insert_node(root.right, value)
        return root

    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        root: Optional[TreeNode] = None
        for value in preorder:
            root = self.insert_node(root, value)
        return root