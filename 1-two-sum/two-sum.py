class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        h_map = {}

        for i in range(n):
            remaining = target - nums[i]
            if remaining in h_map:
                return [h_map[remaining], i]

            h_map[nums[i]] = i
        return [-1, -1] 