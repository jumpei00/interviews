from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 0:
            return True

    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
