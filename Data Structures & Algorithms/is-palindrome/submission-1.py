class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            leftC = s[left]
            rightC = s[right]
            if not leftC.isalnum():
                left += 1
                continue
            if not rightC.isalnum():
                right -= 1
                continue
            
            if leftC.lower() != rightC.lower():
                return False
            
            left += 1
            right -= 1

        return True
        