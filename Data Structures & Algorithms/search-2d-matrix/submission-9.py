class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0]) - 1
        c = 0

        while c < len(matrix):
            if target <= matrix[c][r]:
                for i, _ in enumerate(matrix[c]):
                    if matrix[c][i] == target:
                        return True
                return False
            else:
                l = 0
                r = r = len(matrix[0]) - 1
                c = c + 1 

        return False       

        