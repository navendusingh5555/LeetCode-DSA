class Solution:
    def NSE(self, nums):
        n = len(nums)
        ans = [0]*n
        stack = []
        
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else n
            stack.append(i)
        return ans
    
    def PSE(self, nums):
        n = len(nums)
        ans = [0]*n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(i)
        return ans

    def sumSubarrayMins(self, nums: List[int]) -> int:
        n = len(nums)
        nse = self.NSE(nums)
        pse = self.PSE(nums)
        mod = int(1e9 + 7)
        total_sum = 0

        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            freq = (left * right)
            contri = (freq * nums[i])%mod
            total_sum = (total_sum + contri)%mod
        return total_sum
            
        