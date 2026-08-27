class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.sumAtmostGoal(nums, k) - self.sumAtmostGoal(nums, k-1)
    
    def sumAtmostGoal(self, nums, k):
        if k < 0:
            return 0
        
        left, right = 0, 0
        n = len(nums)
        count = 0
        total_sum = 0

        while right < n:
            total_sum += nums[right]%2

            while total_sum > k:
                total_sum -= nums[left]%2
                left += 1
            
            count += (right - left + 1)

            right += 1
        return count
        