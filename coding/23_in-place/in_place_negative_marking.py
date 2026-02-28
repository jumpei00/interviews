from typing import List


def find_unique(nums: List[int]) -> int:
    n = len(nums)

    for i in range(n):
        nums[abs(nums[i])] *= -1

    unique = -1

    for i in range(n):
        if nums[i] < 0:
            unique = i
            nums[i] = abs(nums[i])
            return unique

    return unique
