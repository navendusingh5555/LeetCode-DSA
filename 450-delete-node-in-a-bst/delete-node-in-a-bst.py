# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None
        if root.val == key:
            return self.deletion(root)
        
        temp = root

        while temp:
            if temp.val > key:
                if temp.left and temp.left.val == key:
                    temp.left = self.deletion(temp.left)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right and temp.right.val == key:
                    temp.right = self.deletion(temp.right)
                    break
                else:
                    temp = temp.right
        return root
    
    def deletion(self, node):
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            right_child = node.right
            last_right = self.findLastRight(node.left)
            last_right.right = right_child
            return node.left
    
    def findLastRight(self, node):
        while node.right:
            node = node.right
        return node
        