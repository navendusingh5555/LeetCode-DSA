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
    
    def PSEE(self, nums):
        n = len(nums)
        ans = [0]*n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(i)
        return ans
    
    def NGE(self, nums):
        n = len(nums)
        ans = [0]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else n
            stack.append(i)
        return ans
    
    def PGEE(self, nums):
        n = len(nums)
        ans = [0]*n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(i)
        return ans
    
    def sumSubarrayMins(self, nums):
        nse = self.NSE(nums)
        psee = self.PSEE(nums)
        n = len(nums)
        total_sum = 0

        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i
            freq = left * right
            contri = freq * nums[i]
            total_sum += contri
        return total_sum
    
    def sumSubarrayMax(self, nums):
        nge = self.NGE(nums)
        pgee = self.PGEE(nums)
        n = len(nums)
        total_sum = 0

        for i in range(n):
            left = i - pgee[i]
            right = nge[i] - i
            freq = left * right
            contri = freq * nums[i]
            total_sum += contri
        return total_sum
    
    def subArrayRanges(self, nums: List[int]) -> int:
        return (self.sumSubarrayMax(nums) - self.sumSubarrayMins(nums))