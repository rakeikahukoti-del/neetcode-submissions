class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = 0
        count = 0

        for number in nums:
            if number == 1:
                temp = temp + 1
            else:
                if temp > count:
                    count = temp
                temp = 0
        
        if temp > count:
            count = temp

        return count