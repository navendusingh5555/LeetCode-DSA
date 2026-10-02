class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]

        for i in range(len(nums) // 2):
            nums[2*i] = pos[i]
            nums[2*i + 1] = neg[i]
        return nums