class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        freq_map = {}

        for i in range(n + 1):
            freq_map[i] = 0
        
        for num in nums:
            freq_map[num] = 1
        
        for key, value in freq_map.items():
            if value == 0:
                return key