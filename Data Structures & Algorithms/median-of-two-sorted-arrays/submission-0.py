class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = (total + 1) // 2

        l, r = 0, len(nums1)
        while l <= r:
            i = (l + r) // 2
            j = half - i

            aLeft = nums1[i - 1] if i > 0 else float("-inf")
            aRight = nums1[i] if i < len(nums1) else float("inf")
            bLeft = nums2[j - 1] if j > 0 else float("-inf")
            bRight = nums2[j] if j < len(nums2) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2 != 0:
                    return max(aLeft, bLeft)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            else:
                if aLeft > bRight:
                    r = i - 1
                else:
                    l = i + 1
