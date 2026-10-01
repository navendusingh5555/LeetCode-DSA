class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1 # Pointer for first zero
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        
        if j == -1:
            return None
        
        for i in range(j+1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1