from typing import List
from copy import deepcopy


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    nums.sort()

    N = len(nums)
    ans = []
    subsets = []

    def rec(i: int):
        if i == N:
            ans.append(deepcopy(subsets))
            return

        num = nums[i]
        j = i

        for k in range(i + 1, N):
            if nums[k] == num:
                j = k
            else:
                break

        num_cnt = j - i + 1

        rec(i + num_cnt)

        for k in range(num_cnt):
            subsets.append(num)
            rec(i + num_cnt)

        for k in range(num_cnt):
            subsets.pop()

        return

    rec(0)

    return ans


if __name__ == "__main__":
    print(subsets_with_dup(nums=[1, 2, 2]))
