from typing import List


def diagonal_sum(mat: List[List[int]]) -> int:
    size = len(mat)
    sum = 0

    for k in range(size):
        sum += mat[k][k]

        # 90度回転した要素を指定
        diagonal_i = k
        diagonal_j = size - k - 1

        # 変換前後で同じ座標であった場合は二重で加算されるのでスキップ
        # これはsizeが奇数の時に対応する
        if k == diagonal_i and k == diagonal_j:
            continue

        sum += mat[diagonal_i][diagonal_j]

    return sum


if __name__ == "__main__":
    print(diagonal_sum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(diagonal_sum(mat=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
