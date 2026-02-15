from typing import List


def max_sum(nums: List[int], k: int) -> int:
    cumulative_sum = [0] * (len(nums) + 1)
    max_s = 0

    for i, num in enumerate(nums):
        cumulative_sum[i + 1] = cumulative_sum[i] + num

    for i in range(len(nums) - k + 1):
        max_s = max(max_s, cumulative_sum[i + k] - cumulative_sum[i])

    return max_s


if __name__ == "__main__":
    print(max_sum([1, 5, 6, 7, 4], 3))  # Output: 18
    print(max_sum([2, 1, 2, 3, 5, 5], 1))  # Output: 5
