class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix) = len(matrix[i]), m = n*n
        # Time Complexity:  O(m)
        # Space Complexity: O(m)
        new_matrix = []
        for col in range(len(matrix[0])):
            new_row = []
            for row in reversed(matrix):
                new_row.append(row[col])
            new_matrix.append(new_row)

        for i in range(len(matrix)):
            matrix[i] = new_matrix[i]
