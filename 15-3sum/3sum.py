class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n < 3:
            return []
        result = set()

        for i in range(0, n - 1):
            my_set = set()
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in my_set:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[j])
        return [list(triplet) for triplet in result]