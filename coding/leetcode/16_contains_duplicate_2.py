from typing import List
from collections import defaultdict


def contains_duplicate_2(nums: List[int], k: int) -> bool:
    duplicate_map = defaultdict(list)

    for i in range(len(nums)):
        value = nums[i]

        if len(duplicate_map[value]) == 0:
            duplicate_map[value] = [0, i]
            continue

        if abs(i - duplicate_map[value][1]) <= k:
            return True

        duplicate_map[value][0] += 1
        duplicate_map[value][1] = i

    return False


def contains_duplicate_v2(nums: List[int], k: int) -> bool:
    duplicatte_hash = {}

    for i, num in enumerate(nums):
        if num in duplicatte_hash and abs(i - duplicatte_hash[num]) <= k:
            return True
        duplicatte_hash[num] = i

    return False


if __name__ == "__main__":
    print(contains_duplicate_v2([1, 2, 3, 1], 3))
    print(contains_duplicate_v2([1, 0, 1, 1], 1))
    print(contains_duplicate_v2([1, 2, 3, 1, 2, 3], 2))
