class Solution:
    def lowerBound(self, nums, target, low, high):
        lb = -1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
    
    def upperBound(self, nums, target, low, high):
        ub = len(nums)
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        lb = self.lowerBound(nums, target, 0, n - 1)

        if lb == -1 or nums[lb] != target:
            return [-1, -1]
        else:
            return [lb, self.upperBound(nums, target, 0, n - 1) - 1]

            