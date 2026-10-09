class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0
        low, high = 0, x

        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid <= x:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result