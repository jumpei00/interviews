from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    index_map = {}

    for i, num in enumerate(nums):
        if num in index_map:
            return [index_map[num], i]
        index_map[target - num] = i

    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
