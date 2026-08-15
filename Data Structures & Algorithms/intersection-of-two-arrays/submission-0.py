class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        res = []

        for num in nums1:
            seen.add(num)
        
        for num in nums2:
            if num in res:
                continue
            elif num in seen:
                res.append(num)
        return res