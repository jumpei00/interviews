from typing import List
from collections import defaultdict


def contains_duplicate(nums: List[int]) -> bool:
    counter_map = defaultdict(int)
    for i in range(len(nums)):
        counter_map[nums[i]] += 1
        if counter_map[nums[i]] == 2:
            return True
    return False

def contains_duplicate_v2(nums: List[int]) -> bool:
	nums_set = set(nums)
	return len(nums) != len(nums_set)


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print(contains_duplicate_v2([1, 2, 3, 1]))
