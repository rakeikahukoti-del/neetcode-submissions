class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = {}
        maxi = 0
        final = 0

        for num in nums:
            if num not in temp:
                temp[num] = 1
            else:
                temp[num] = temp.get(num) + 1
        
        for num, count in temp.items():
            print(num, count)
            
            if count > maxi:
                maxi = count
                final = num
        
        return final
