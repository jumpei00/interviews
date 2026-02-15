from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    n = len(nums)
    left, right = 0, n - 1

    result = [-1] * n

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            result[i] = nums[right] ** 2
            right -= 1
        else:
            result[i] = nums[left] ** 2
            left += 1

    return result
