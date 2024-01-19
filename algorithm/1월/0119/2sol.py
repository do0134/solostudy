# Leetcode 240. Search a 2D Matrix II

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 136 ms
        n = len(matrix)
        m = len(matrix[0])

        r = n - 1
        c = 0

        while 0 <= r and c < m:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1

        return False

        """
        150 ms
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True

        return False
        """