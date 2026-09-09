class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '{': 
                stack.append(c)
            if c == '(':
                stack.append(c)
            if c == '[':
                stack.append(c)
            if len(stack) == 0 and c in [')', '}', ']']:
                return False
            if c == '}':
                stack_top = stack.pop()
                if stack_top != '{':
                    return False
            if c == ']':
                stack_top = stack.pop()
                if stack_top != '[':
                    return False
            if c == ')':
                stack_top = stack.pop()
                if stack_top != '(':
                    return False
        return len(stack) == 0
        