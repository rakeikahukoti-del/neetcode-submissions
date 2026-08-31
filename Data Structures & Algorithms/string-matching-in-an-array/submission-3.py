class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        temp = set()

        for word in words:

            for i in range(len(words)):
                if word == words[i]:
                    continue
                elif word in words[i]:
                    temp.add(word)
        
        return list(temp)
