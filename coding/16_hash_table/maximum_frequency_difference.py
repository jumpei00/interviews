from typing import List
from collections import defaultdict


def maximum_frequency_difference(nums: List[int]) -> int:
    counter_map = defaultdict(int)
    most_frequency_diff_count = 0

    for i in range(len(nums) - 1):
        diff = abs(nums[i] - nums[i + 1])
        counter_map[diff] += 1

        if counter_map[diff] > most_frequency_diff_count:
            most_frequency_diff_count = counter_map[diff]

    return most_frequency_diff_count


if __name__ == "__main__":
    print(maximum_frequency_difference([1, 2, 3, 2, 1]))
    print(maximum_frequency_difference([1, 5, 2, 3, 6]))
