# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root):
        self.stack1 = []
        self.stack2 = []
        self._pushAllLeft(root)
        self._pushAllRight(root)
    
    def _pushAllLeft(self, root):
        while root:
            self.stack1.append(root)
            root = root.left
    
    def _pushAllRight(self, root):
        while root:
            self.stack2.append(root)
            root = root.right
    
    def next(self):
        node = self.stack1.pop()
        if node.right:
            self._pushAllLeft(node.right)
        return node.val
    
    def before(self):
        node = self.stack2.pop()
        if node.left:
            self._pushAllRight(node.left)
        return node.val


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        iter = BSTIterator(root)
        i = iter.next()
        j = iter.before()

        while i < j:
            if i + j == k:
                return True
            elif i + j < k:
                i = iter.next()
            else:
                j = iter.before()
        return False