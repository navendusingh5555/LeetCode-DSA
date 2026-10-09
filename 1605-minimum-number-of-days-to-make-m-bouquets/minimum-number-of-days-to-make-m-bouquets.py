class Solution:
    def can_make_bouquets(self, bloomDay, day, m, k):
        consecutive = 0
        bouquets = 0

        for bloom in bloomDay:
            if bloom <= day:
                consecutive += 1
                if consecutive == k:
                    bouquets += 1
                    consecutive = 0
            else:
                consecutive = 0
        return bouquets >= m

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            if self.can_make_bouquets(bloomDay, mid, m, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans