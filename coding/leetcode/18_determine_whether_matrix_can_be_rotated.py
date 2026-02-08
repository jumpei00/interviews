from typing import List


def find_rotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    size = len(mat)

    is0OK = True
    is90OK = True
    is180OK = True
    is270OK = True

    for i in range(size):
        for j in range(size):
            if mat[i][j] != target[i][j]:
                is0OK = False
            if mat[i][j] != target[j][size - i - 1]:
                is90OK = False
            if mat[i][j] != target[size - i - 1][size - j - 1]:
                is180OK = False
            if mat[i][j] != target[size - j - 1][i]:
                is270OK = False

            if not is0OK and not is90OK and not is180OK and not is270OK:
                return False

    return True


if __name__ == "__main__":
    print(find_rotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]]))
    print(find_rotation(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]]))
    print(
        find_rotation(
            mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]],
            target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]],
        )
    )
