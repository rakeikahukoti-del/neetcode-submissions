class Solution:
    def findLucky(self, arr: List[int]) -> int:
        temp = {}
        current = -1

        for num in arr:
            if num not in temp:
                temp[num] = 1
            else:
                temp[num] = temp[num] + 1
        
        for num, count in temp.items():
            if (num == count) and num > current:
                current = num
                
            
        return current