class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dist1, dist2 = [], []

        for num in set(nums1):
            if num in set(nums2):
                pass
            else:
                dist1.append(num)
        
        for num in set(nums2):
            if num in set(nums1):
                pass
            else:
                dist2.append(num)
        
        return [dist1, dist2]