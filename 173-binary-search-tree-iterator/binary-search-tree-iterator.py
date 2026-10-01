# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.nodesSorted = []
        self.index = 0
        self._inorder(root)
    
    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodesSorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        val = self.nodesSorted[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.nodesSorted)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()