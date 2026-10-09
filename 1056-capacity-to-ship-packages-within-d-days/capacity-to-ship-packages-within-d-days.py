class Solution:
    def days_needed(self, weights, days, capacity):
        used_days = 1
        curr_load = 0

        for weight in weights:
            if curr_load + weight > capacity:
                used_days += 1
                curr_load = weight
            else:
                curr_load += weight
        return used_days <= days

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        result = high

        while low <= high:
            mid = low + (high - low) // 2

            if self.days_needed(weights, days, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result