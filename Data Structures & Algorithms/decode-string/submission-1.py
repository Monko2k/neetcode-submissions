class Solution:
    def decodeString(self, s: str) -> str:
        INT_0 = '0'
        INT_9 = '9'

        res = []

        def expand(x, curRes):
            i = x
            countChar = []
            while i < len(s):
                c = s[i]
                if INT_0 <= c <= INT_9:
                    countChar.append(c)
                    i += 1
                elif c == '[':
                    count = int(''.join(countChar))
                    countChar = []
                    layer = []
                    i = expand(i + 1, layer)
                    curRes += count * layer
                elif c == ']':
                    return i + 1
                else:
                    curRes.append(c)
                    i += 1
        expand(0, res)
        return ''.join(res)




        