class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = []

        for word in s.split():
            temp.append(word)

        return len(temp[-1])
            

