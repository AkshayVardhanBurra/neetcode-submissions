class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rowSize = len(matrix[0])
        totalSize = len(matrix) * rowSize
        
        left, right = 0, totalSize - 1

        while left <= right:

            mid = int((left + right)/2)
            row = int(mid/rowSize)
            ind = mid % rowSize
            if matrix[row][ind] == target:
                return True
            elif target > matrix[row][ind]:
                left = mid + 1
            else:
                right = mid - 1
        return False
        