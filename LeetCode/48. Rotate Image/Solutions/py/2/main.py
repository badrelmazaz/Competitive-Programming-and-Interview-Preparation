class Solution:

    def transpose(self, matrix: List[List[int]]) -> None:
        # n = len(matrix) = len(matrix[i]), m = n*n
        # Time Complexity:  O(m)
        # Space Complexity: O(1)

        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix) = len(matrix[i]), m = n*n
        # Time Complexity:  O(m)
        # Space Complexity: O(1)
        
        self.transpose(matrix)
        # reverse each row
        for row in matrix:
            row.reverse()