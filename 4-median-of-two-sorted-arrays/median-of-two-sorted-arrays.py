class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_num = []

        for val in nums1:
            merged_num.append(val)
        for val in nums2:
            merged_num.append(val)
        
        merged_num.sort()

        n = len(merged_num)

        if n % 2 == 1:
            return float(merged_num[n // 2])
        else:
            return (merged_num[n // 2 - 1] + merged_num[n // 2]) / 2.0