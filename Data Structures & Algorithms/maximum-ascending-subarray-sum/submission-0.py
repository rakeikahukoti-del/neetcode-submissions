class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                curr = 0
            
            curr += nums[i]
            maxi = max(maxi, curr)


        return maxi