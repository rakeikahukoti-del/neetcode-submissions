class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = []
        
        for i in range(0, len(nums)):
            if (i + 1) in nums:
                continue
            else:
                temp.append(i + 1)
                
        return temp