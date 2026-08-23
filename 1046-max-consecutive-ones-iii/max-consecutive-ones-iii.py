class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len = 0
        left, right = 0, 0
        zeroes = 0

        while right < n:
            if nums[right] == 0:
                zeroes += 1
            if zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            if zeroes <= k:
                max_len = max(max_len, right-left+1)
            right += 1
        return max_len
        