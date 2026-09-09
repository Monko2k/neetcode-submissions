class Solution:

    def numDecodings(self, s: str) -> int:
        decodeOne = 1
        decodeTwo = 0
        
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            cur = 0
            if char != '0':
                cur += decodeOne
                if i + 1 < len(s) and int(char + s[i + 1]) <= 26:
                    cur += decodeTwo
            decodeTwo = decodeOne
            decodeOne = cur


        return decodeOne
            



    
        