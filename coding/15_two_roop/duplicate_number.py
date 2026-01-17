from typing import List


def has_duplicate(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 1]))
    print(has_duplicate([1, 2, 3, 4, 6]))
