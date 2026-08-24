class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left, right = 0, 0
        freq = {}
        max_freq = 0
        max_len = 0

        while right < n:
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            if (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            
            if (right - left + 1) - max_freq <= k:
                max_len = max(max_len, right-left+1)
            
            right += 1
        return max_len

        