from typing import List


def has_consecutive_numbers(nums: List[int]) -> bool:
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 1:
            return True

    return False


if __name__ == "__main__":
    print(has_consecutive_numbers([4, 1, 5]))
    print(has_consecutive_numbers([4, 1, 6]))
