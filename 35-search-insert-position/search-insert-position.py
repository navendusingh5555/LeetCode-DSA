class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        index = n

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= target:
                index = min(index, mid)
                high = mid - 1
            else:
                low = mid + 1
        return index