class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr_depth = 0
        st = []

        for char in s:
            if char == "(":
                st.append(char)
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif char == ")":
                st.pop()
                curr_depth -= 1
        return max_depth