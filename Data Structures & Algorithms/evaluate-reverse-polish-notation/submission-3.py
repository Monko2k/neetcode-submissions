class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "/", "*"]:
                stack.append(int(token))
                continue
                
            o1 = stack.pop()
            o2 = stack.pop()
            if token == "+":
                stack.append(o2 + o1)
            if token == "-":
                stack.append(o2 - o1)
            if token == "*":
                stack.append(o2 * o1)
            if token == "/":
                stack.append(int(o2 / o1))
            
        return stack[0]