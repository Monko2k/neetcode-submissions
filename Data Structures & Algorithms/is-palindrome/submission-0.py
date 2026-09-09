class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s).lower()
        mid = len(s) // 2
        l1 = s[:mid]
        l2 = s[mid:]
        l2 = l2[::-1]
        print(l1)
        print(l2)
        for i, c in enumerate(l1):
            if c != l2[i]:
                return False

        return True
        