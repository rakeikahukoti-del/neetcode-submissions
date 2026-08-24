class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        temp = []
        maxi = 0

        for n in nums:
            
            if n in temp:
                temp.remove(n)
            else:
                temp.append(n)
        
        if len(temp) == 0:
            return -1

        for num in temp:
            if num > maxi:
                maxi = num

        return maxi
        

        
