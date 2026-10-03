class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt = 0
        one_cnt = 0
        two_cnt = 0

        for num in nums:
            if num == 0:
                zero_cnt += 1
            elif num == 1:
                one_cnt += 1
            else:
                two_cnt += 1
        
        ind = 0
        for _ in range(zero_cnt):
            nums[ind] = 0
            ind += 1
        for _ in range(one_cnt):
            nums[ind] = 1
            ind += 1
        for _ in range(two_cnt):
            nums[ind] = 2
            ind += 1