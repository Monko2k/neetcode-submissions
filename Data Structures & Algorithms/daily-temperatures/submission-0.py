class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            temp = temperatures[i]

            while len(stack) > 0:
                stackTop = stack[-1]
                if stackTop[0] < temp:
                    stack.pop()
                    stackIdx = i - stackTop[1]
                    res[stackTop[1]] = stackIdx
                else:
                    break

            stack.append((temp, i))
        return res

        