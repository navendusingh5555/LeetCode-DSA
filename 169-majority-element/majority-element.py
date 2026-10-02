class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        h_map = {}

        for num in nums:
            h_map[num] = h_map.get(num, 0) + 1
        
        for key, value in h_map.items():
            if value > n//2:
                return key