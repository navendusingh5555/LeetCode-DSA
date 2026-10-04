class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}

        for char in s:
            map_s[char] = map_s.get(char, 0) + 1
        
        for char in t:
            if char not in map_s:
                return False
            else:
                if map_s[char] == 0:
                    return False
                else:
                    map_s[char] -= 1
        return True