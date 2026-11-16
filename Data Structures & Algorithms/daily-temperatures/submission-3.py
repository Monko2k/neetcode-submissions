class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while len(stack) > 0:
                topVal, topIdx = stack[-1]
                if topVal < temp:
                    stack.pop()
                    res[topIdx] = i - topIdx
                else:
                    break

            stack.append((temp, i))
        return res

        