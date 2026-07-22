import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        elements = nums.copy()
        
        for num in nums:
            elements.remove(num)
            products.append(math.prod(elements))
            elements.append(num)
        
        return products