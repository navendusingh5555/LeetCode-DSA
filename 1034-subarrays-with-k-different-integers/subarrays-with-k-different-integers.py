class Solution:
    def atMost(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        count = 0
        freq = dict()

        while right < len(nums):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while len(freq) > k:
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            count += right - left + 1
            right += 1
        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)
        