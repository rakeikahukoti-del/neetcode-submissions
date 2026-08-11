class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        close_chars = (')', '}', ']')
        open_of_close = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in close_chars:
                if len(stk) == 0:
                    return False
                o = stk.pop()
                if open_of_close[c] != o:
                    return False
                continue
            
            stk.append(c)

        return len(stk) == 0