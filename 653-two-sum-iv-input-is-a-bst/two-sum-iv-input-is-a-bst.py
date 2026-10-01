# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, nums):
        if not root:
            return
        self.inorder(root.left, nums)
        nums.append(root.val)
        self.inorder(root.right, nums)
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        self.inorder(root, nums)

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == k:
                return True
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return False