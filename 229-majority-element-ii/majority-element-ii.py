class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cand1, cand2 = None, None
        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = num, 1
            elif cnt2 == 0:
                cand2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        result = []
        n = len(nums)
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > n//3:
                result.append(cand)

        return result