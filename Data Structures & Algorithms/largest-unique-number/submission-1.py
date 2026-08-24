class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        temp = []

        for n in nums:
            
            if n in temp:
                temp.remove(n)
            else:
                temp.append(n)

        return -1 if len(temp) == 0 else max(temp)