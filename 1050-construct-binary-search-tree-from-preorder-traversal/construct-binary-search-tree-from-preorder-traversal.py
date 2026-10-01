# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, preorder, limit):
        if not preorder:
            return None
        if self.index >= len(preorder):
            return None
        value:int = preorder[self.index]

        if not limit[0] <= value <= limit[1]:
            return None
        
        root = TreeNode(value)
        self.index += 1

        root.left = self.build(preorder, [limit[0], value])
        root.right = self.build(preorder, [value, limit[1]])

        return root

    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        self.index:int = 0
        return self.build(preorder, [float("-inf"), float("inf")])