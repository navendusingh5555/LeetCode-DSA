# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        cnt = 0
        ans = None
        def traverse(node):
            nonlocal cnt, ans
            if not node or ans is not None:
                return
            traverse(node.left)

            cnt += 1
            if cnt == k:
                ans = node.val
                return
            traverse(node.right)
        traverse(root)
        return ans