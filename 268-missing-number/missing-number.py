class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        total_sum = sum(nums)
        exp_sum = n * (n + 1) // 2

        return exp_sum - total_sum