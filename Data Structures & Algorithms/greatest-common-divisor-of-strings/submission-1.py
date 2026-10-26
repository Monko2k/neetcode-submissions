class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        g = math.gcd(len(str1), len(str2))

        for i in range(len(str1)):
            if str1[i] != str1[i % g]:
                return ""
        for i in range(len(str2)):
            if str2[i] != str1[i % g]:
                return ""

        return str1[:g]
        