class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            if c in [')', '}', ']']:
                if len(stack) == 0: 
                    return False
                top = stack.pop()
                if c == ')' and top != '(':
                    return False
                if c == ']' and top != '[':
                    return False
                if c == '{' and top != '}':
                    return False
        return len(stack) == 0
                

        