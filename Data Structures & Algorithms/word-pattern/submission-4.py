class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sentence = list(s.split())
        word = list(pattern)
        res = {}

        if len(sentence) != len(word):
            return False

        for i in range(len(sentence)):
            res[word[i]] = sentence[i]
        
        print(res)

        for j in range(len(word)):
            if len(res) != len(set(res.values())):
                return False
            elif res.get(word[j]) ==  sentence[j]:
                continue
            else:
                return False
        
        
        
        return True