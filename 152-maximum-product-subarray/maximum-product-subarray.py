class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        result = float("-inf")
        curr_max = 1
        curr_min = 1

        for num in nums:
            prev_max = curr_max
            prev_min = curr_min

            curr_max = max(prev_max * num, num, prev_min * num)
            curr_min = min(prev_max * num, num, prev_min * num)

            result = max(result, curr_max)
            
        return result