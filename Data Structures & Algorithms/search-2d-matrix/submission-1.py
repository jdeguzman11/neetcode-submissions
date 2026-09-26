class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        cols = len(matrix[0])

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid // cols][mid % cols] > target:
                r = mid - 1
            
            elif matrix[mid // cols][mid % cols] < target:
                l = mid + 1
            
            else:
                return True
        
        return False