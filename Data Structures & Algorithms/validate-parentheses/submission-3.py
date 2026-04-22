class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return False
        opened = ['(', '{', '[']
        closed = [')', '}', ']']
        stack = []
        for char in s:
            if char in opened:
                stack.append(char)
            elif char in closed:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if not closed.index(char) == opened.index(last):
                    return False
        if len(stack) is not 0:
            return False
        return True 
