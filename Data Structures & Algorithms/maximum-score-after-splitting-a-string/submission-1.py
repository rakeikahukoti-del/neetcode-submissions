class Solution:
    def maxScore(self, s: str) -> int:
        res = []

        for i in range(1,len(s)):
            temp = 0

            left = s[:i]
            for j in range(len(left)):
                if left[j] == "0":
                    temp = temp + 1

            right = s[i:]
            for j in range(len(right)):
                if right[j] == "1":
                    temp = temp + 1
            
            res.append(int(temp))
        return max(res)