from typing import List
from copy import deepcopy


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()

    N = len(candidates)
    ans = []

    temp_array = []

    def rec(rest, i):
        if rest == 0:
            ans.append(deepcopy(temp_array))
            return

        for j in range(i, N):
            num = candidates[j]
            if num > rest:
                break
            temp_array.append(num)
            rec(rest - num, j)
            temp_array.pop()

    rec(target, 0)

    return ans


if __name__ == "__main__":
    print(combination_sum(candidates=[2, 3, 6, 7], target=7))
    print(combination_sum(candidates=[2, 3, 5], target=8))
    print(combination_sum(candidates=[2], target=1))
    print(combination_sum(candidates=[1], target=4))
