class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        max_len = 0
        left, right = 0, 0
        my_dict = dict()

        while right < n:
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1

            if len(my_dict) > 2:
                my_dict[fruits[left]] -= 1
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1
            
            if len(my_dict) <= 2:
                max_len = max(max_len, right-left+1)
            
            right += 1
        return max_len