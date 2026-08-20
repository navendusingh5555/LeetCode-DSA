class Solution:
    def NSE(self, heights):
        n = len(heights)
        ans = [0]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else n
            stack.append(i)
        return ans
    
    def PSE(self, heights):
        n = len(heights)
        ans = [0]*n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(i)
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse = self.NSE(heights)
        pse = self.PSE(heights)
        area = 0
        max_area = 0
        for i in range(n):
            area = (nse[i] - pse[i] - 1) * heights[i]
            max_area = max(max_area, area)
        return max_area
        