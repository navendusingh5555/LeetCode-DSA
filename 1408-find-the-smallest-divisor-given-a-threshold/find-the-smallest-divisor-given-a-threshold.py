class Solution:
    def is_small_enough(self, nums, divisor, threshold):
        total_sum = 0
        for num in nums:
            total_sum += (num + divisor - 1) // divisor
            
            if total_sum > threshold:
                return False
        return total_sum <= threshold

    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        total = sum(nums)
        if threshold >= total:
            return 1
        if threshold == len(nums):
            return max(nums)
        
        low = 1
        high = max(nums)

        while low < high:
            mid = low + (high - low) // 2

            if self.is_small_enough(nums, mid, threshold):
                high = mid
            else:
                low = mid + 1
        return low