from typing import List


def count_nums(nums: List[int]) -> List[int]:
    n = len(nums)

    for i in range(n):
        num = nums[i] % n
        nums[num] += n

    for i in range(n):
        nums[i] //= n

    return nums
