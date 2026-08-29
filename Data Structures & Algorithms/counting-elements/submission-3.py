class Solution:
    def countElements(self, arr: List[int]) -> int:
        temp = set(arr)
        count = 0

        for num in arr:
            if (num + 1) in temp:
                count = count + 1
        
        return count