# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_ptr = 0

        for i in range(1, len(preorder)):
            val = preorder[i]
            node = stack[-1]

            if node.val != inorder[inorder_ptr]:
                node.left = TreeNode(val)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorder_ptr]:
                    node = stack.pop()
                    inorder_ptr += 1
                node.right = TreeNode(val)
                stack.append(node.right)
        return root