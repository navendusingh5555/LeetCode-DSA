class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.withSumAtmostGoal(nums, goal) - self.withSumAtmostGoal(nums, goal-1)

    def withSumAtmostGoal(self, nums, goal):
        if goal < 0:
            return 0
            
        left, right = 0, 0
        total_sum = 0
        count = 0
        n = len(nums)

        while right < n:
            total_sum += nums[right]

            while total_sum > goal:
                total_sum -= nums[left]
                left += 1
                
            count += (right - left + 1)
            right += 1

        return count