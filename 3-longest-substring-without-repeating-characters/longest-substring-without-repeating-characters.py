class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        my_dict = dict()
        left, right = 0, 0
        n = len(s)

        while right < n:
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1)
            max_len =max(max_len, right-left+1)
            my_dict[s[right]] = right
            right += 1
        return max_len 
        