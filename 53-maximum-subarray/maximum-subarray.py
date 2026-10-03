class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum = float("-inf")
        total = 0

        for num in nums:
            total += num
            max_sum = max(max_sum, total)

            if total < 0:
                total = 0
        return max_sum