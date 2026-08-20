class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = []
        result = ""

        for digit in nums:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        while stack and k > 0:
            stack.pop()
            k -= 1
        
        if not stack:
            return "0"
        
        while stack:
            result += stack.pop()
        
        result = result.rstrip("0")
        result = result[::-1]

        if not result:
            return "0"
        
        return result
