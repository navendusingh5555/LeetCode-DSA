class Solution:
    def solve(self, nums, low, high, target):
        if low > high:
            return -1
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.solve(nums, mid + 1, high, target)
        else:
            return self.solve(nums, low, mid - 1, target)
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        return self.solve(nums, 0, n - 1, target)