class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        cols = len(matrix[0])

        while l <= r:
            middle = (r + l) // 2

            if matrix[middle // cols][middle % cols] > target:
                r = middle - 1
            
            elif matrix[middle // cols][middle % cols] < target:
                l = middle + 1
            
            else:
                return True
                
        return False


                
            