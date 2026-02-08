from typing import List


def rotate(matrix: List[List[int]]) -> None:
    size = len(matrix)

    for i in range(size // 2):
        for j in range(i, size - i - 1):
            temp_right_top = matrix[j][size - i - 1]
            matrix[j][size - i - 1] = matrix[i][j]

            temp_right_buttom = matrix[size - i - 1][size - j - 1]
            matrix[size - i - 1][size - j - 1] = temp_right_top

            temp_left_buttom = matrix[size - j - 1][i]
            matrix[size - j - 1][i] = temp_right_buttom

            matrix[i][j] = temp_left_buttom

    return None


if __name__ == "__main__":
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix)
    print(matrix)
