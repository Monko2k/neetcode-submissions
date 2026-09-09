class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 1
        freq = defaultdict(int)
        maxFreq = 1
        freq[s[0]] = 1
        l = 0
        r = l + 1
        while r < len(s):
            c = s[r]
            freq[c] += 1
            maxFreq = max(freq[c], maxFreq)
            while (r - l + 1) - maxFreq > k:
                l_char = s[l]
                freq[l_char] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen


            



        