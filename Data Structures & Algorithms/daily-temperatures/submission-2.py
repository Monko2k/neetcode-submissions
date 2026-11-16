class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            temp = temperatures[i]

            while len(stack) > 0:
                stackTop = stack[-1]
                topVal, topIdx = stack[-1]
                if topVal < temp:
                    stack.pop()
                    diff = i - topIdx
                    res[topIdx] = diff
                else:
                    break

            stack.append((temp, i))
        return res

        