class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A                      # binary search the shorter one

        m, n = len(A), len(B)
        left_size = (m + n + 1) // 2         # left half gets the extra element if odd

        lo, hi = 0, m                        # possible values of a_count
        while lo <= hi:
            a_count = (lo + hi) // 2         # how many elements A puts in the left half
            b_count = left_size - a_count    # B fills the rest

            a_left  = A[a_count - 1] if a_count > 0 else float("-inf")
            a_right = A[a_count]     if a_count < m else float("inf")
            b_left  = B[b_count - 1] if b_count > 0 else float("-inf")
            b_right = B[b_count]     if b_count < n else float("inf")

            if a_left <= b_right and b_left <= a_right:   # valid cut
                if (m + n) % 2 == 1:
                    return max(a_left, b_left)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                hi = a_count - 1             # A gave too many, take fewer
            else:
                lo = a_count + 1             # A gave too few, take more