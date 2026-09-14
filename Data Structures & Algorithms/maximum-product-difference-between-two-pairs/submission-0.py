class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        two_highest = sorted(nums, reverse=True)[:2]
        two_lowest = sorted(nums)[:2]

        return (two_highest[0] * two_highest[1]) - (two_lowest[0] * two_lowest[1])
