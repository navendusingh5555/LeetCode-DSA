class Solution:
    def count_subarrays(self, nums, max_allowed):
        subarrays = 1
        curr_sum = 0

        for num in nums:
            if curr_sum + num > max_allowed:
                subarrays += 1
                curr_sum = num
            else:
                curr_sum += num
        return subarrays

    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        result = high

        while low <= high:
            mid = low + (high - low) // 2

            if self.count_subarrays(nums, mid) <= k:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result