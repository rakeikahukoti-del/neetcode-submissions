class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ht1 = {}
        ht2 = {}

        for char in s:
            if char in ht1:
                ht1[char] = ht1[char] + 1
            else:
                ht1[char] = 1
            
        for char in t:
            if char in ht2:
                ht2[char] = ht2[char] + 1
            else:
                ht2[char] = 1
        
        if ht1 == ht2:
            return True

        return False