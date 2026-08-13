class Solution:
    def scoreOfString(self, s: str) -> int:
        temp = 0

        for i in range(1,len(s)):
            temp = temp + abs((ord(s[i]) - ord(s[i-1])))

        return temp