class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        h_map = {}
        result = []

        for num in nums:
            h_map[num] = h_map.get(num, 0) + 1
        
        for key, value in h_map.items():
            if value > n//3:
                result.append(key)
            if len(result) == 2:
                break
        return result