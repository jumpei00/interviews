from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    left_cumulative_nums = [1] * (n + 1)
    right_cumulative_nums = [1] * (n + 1)

    for i in range(n):
        left_cumulative_nums[i + 1] = left_cumulative_nums[i] * nums[i]
        right_cumulative_nums[i + 1] = right_cumulative_nums[i] * nums[n - 1 - i]

    for i in range(n):
        nums[i] = left_cumulative_nums[i] * right_cumulative_nums[n - 1 - i]

    return nums


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))
    print(product_except_self([-1, 1, 0, -3, 3]))
