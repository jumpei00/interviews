from typing import List


def longest_consecutive_sequence(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    nums.sort()

    longest_consecutive_num = 0
    consecutive_num = 1

    current = nums[0]
    for i in range(1, len(nums)):
        if nums[i] - current == 1:
            consecutive_num += 1

        if nums[i] - current >= 2:
            longest_consecutive_num = max(longest_consecutive_num, consecutive_num)
            consecutive_num = 1

        current = nums[i]

    return max(longest_consecutive_num, consecutive_num)


if __name__ == "__main__":
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(longest_consecutive_sequence([1, 0, 1, 2]))
    print(longest_consecutive_sequence([1, 2, 6, 7, 8]))
