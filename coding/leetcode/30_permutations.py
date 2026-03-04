from typing import List
from copy import deepcopy


def permute(nums: List[int]) -> List[List[int]]:
    ans = []
    subsets = []
    nums_set = set(nums)

    def _permute():
        if len(nums_set) == 0:
            ans.append(deepcopy(subsets))
            return

        rest_nums = list(nums_set)

        for num in rest_nums:
            nums_set.remove(num)
            subsets.append(num)

            _permute()

            subsets.pop()
            nums_set.add(num)

        return

    _permute()

    return ans
