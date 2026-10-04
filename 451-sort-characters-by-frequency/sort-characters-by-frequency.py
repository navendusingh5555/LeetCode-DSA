class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        h_map = {}

        for char in s:
            h_map[char] = h_map.get(char, 0) + 1
        
        for char, freq in sorted(h_map.items(), key = lambda item : item[1], reverse = True):
            result += (char * freq)
        
        return result