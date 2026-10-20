class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(B) < len(A):
            A, B = B, A
        
        m = len(A)
        n = len(B)
        
        mid = (m + n + 1) // 2
        l = 0 
        r = m
        while l <= r:
            cut_a = (l + r) // 2
            cut_b = mid - cut_a

            A_left = A[cut_a - 1] if cut_a > 0 else -math.inf
            A_right = A[cut_a] if cut_a < m else math.inf
            B_left = B[cut_b - 1] if cut_b > 0 else -math.inf
            B_right = B[cut_b] if cut_b < n else math.inf

            if A_left > B_right:
                r = cut_a - 1
            elif B_left > A_right:
                l = cut_a + 1
            else:
                if (m + n) % 2:
                    return max(B_left, A_left)
                return (max(B_left, A_left) + min(B_right, A_right))/2

                
            


        