class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0]*n
        pos_ind = 0
        neg_ind = 1

        
        for num in nums:
            if num > 0:
                ans[pos_ind] = num
                pos_ind += 2
            else:
                ans[neg_ind] = num
                neg_ind += 2
        return ans