# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""
        
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("#")
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None
            
        vals = data.split(",")
            
        root = TreeNode(int(vals[0]))

        queue = deque([root])

        i = 1

        while queue and i < len(vals):
            curr = queue.popleft()

            if vals[i] != "#":
                left_node = TreeNode(int(vals[i]))
                curr.left = left_node
                queue.append(left_node)
            i += 1

            if vals[i] != "#":
                right_node = TreeNode(int(vals[i]))
                curr.right = right_node
                queue.append(right_node)
            i += 1
            
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))