from typing import List


def is_matrix_rotated(matrix: List[List[int]], target: List[List[int]]) -> bool:
    n = len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != target[j][n - i - 1]:
                return False
    return True


if __name__ == "__main__":
    print(
        is_matrix_rotated(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        )
    )
    print(
        is_matrix_rotated(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        )
    )
