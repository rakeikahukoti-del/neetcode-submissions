class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for i in range(len(shift)):
            if shift[i][0] == 0:
                s = s[shift[i][1]:] + s[:shift[i][1]]
            
            if shift[i][0] == 1:
                s= s[-shift[i][1]:] + s[:-shift[i][1]]
        return s