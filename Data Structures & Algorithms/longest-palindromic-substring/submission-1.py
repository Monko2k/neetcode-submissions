class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestLeft = 0
        bestRight = 0

        for i in range(len(s)):
            for left, right in ((i, i), (i, i + 1)):
                while (
                    left >= 0
                    and right < len(s)
                    and s[left] == s[right]
                ):
                    left -= 1
                    right += 1

                left += 1
                right -= 1

                if right - left > bestRight - bestLeft:
                    bestLeft = left
                    bestRight = right

        return s[bestLeft:bestRight + 1]