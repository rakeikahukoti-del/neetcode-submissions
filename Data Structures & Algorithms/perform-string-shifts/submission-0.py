class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        for i in range(len(shift)):
            print(shift[i][1])

            if shift[i][0] == 0: #Left
                s = s[shift[i][1]:] + s[:shift[i][1]]
            
            if shift[i][0] == 1: #Right
                s= s[-shift[i][1]:] + s[:-shift[i][1]]
        
            print(s)

        return s
