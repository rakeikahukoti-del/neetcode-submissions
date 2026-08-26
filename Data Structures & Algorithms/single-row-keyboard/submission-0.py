class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        prev = 0
        total = 0

        
        for i in range(0,len(word)):
            count = 0

            for x in range(0,len(keyboard)):
                if keyboard[x] == word[i]:
                    if prev > x:
                        total = total + (prev - x)
                        prev = x
                    else:
                        total = total + (x - prev)
                        prev = x
                    
                    break
        
        return total