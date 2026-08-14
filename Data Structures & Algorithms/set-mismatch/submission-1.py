class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = 0
        missing = 0

        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)
        
        for num in range(1, len(nums) + 1):
            if num not in seen:
                missing = num
                break
        
        return [duplicate, missing]